import os
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import re  # To extract the timestamp from the file name

############# Plotting ########
pgf_with_latex = {                      # setup matplotlib to use latex for output
    "pgf.texsystem": "pdflatex",        # change this if using xetex or lautex
    "text.usetex": True,                # use LaTeX to write all text
    "pgf.preamble": "\n".join( [
        r"\usepackage[utf8x]{inputenc}",    # use utf8 fonts 
        r"\usepackage[T1]{fontenc}",        # plots will be generated
        r"\usepackage{amsmath}",
        r"\usepackage{siunitx}",
        ])                                   # using this preamble
    }

mpl.use("pgf")
mpl.rcParams.update(pgf_with_latex)


def get_next_filename(folder: str, prefix: str, extension: str, timestamp: str) -> str:
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"{prefix}_{timestamp}.{extension}")
    return filename


# Loop through files in the channels folder (one level up)
channels_folder = os.path.join(os.getcwd(), '..', 'channels')
output_folder = os.path.join(os.getcwd(), '..', 'plots')

for filename in os.listdir(channels_folder):
    if filename.endswith('.csv'):  # Check if it's a CSV file
        file_path = os.path.join(channels_folder, filename)
        
        # Extract timestamp from the filename (assuming format: channel_Y-M-D_H-M-S.csv)
        match = re.match(r'channel_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})\.csv', filename)
        if match:
            timestamp = match.group(1)
        else:
            continue  # Skip files that don't match the expected format
        
        df = pd.read_csv(file_path, header=None)
        t = df[0]*1E3
        ue = df[1]*1E3
        ua = df[2]*1E3

        plt.plot(t, ue, label = "$u_e$", color='orange')
        plt.plot(t, ua, label = "$u_a$", color='blue')

        ax = plt.gca()
        ax.set_xlabel('Zeit in \\unit{\\ms}', labelpad = 5)
        ax.set_ylabel("Spannung in \\unit{\\mV}", labelpad = 0)
        
        # mark peak voltages with horizontal lines
        ax.axhline(np.max(ua), linestyle='--', linewidth=1, color='blue')
        ax.axhline(np.max(ue), linestyle='--', linewidth=1, color='orange')

        plt.legend()

        # add text box for the statistics
        stats = (f'$u_e$ = {np.max(ue):.2f}' + ' \\unit{\\mV}' + '\n'
                 f'$u_a$ = {np.max(ua):.2f}' + ' \\unit{\\mV}')

        plt.gcf().text(1.025, 0.9, stats, transform=ax.transAxes, horizontalalignment='left', fontsize=12, \
                       bbox = dict(boxstyle='round', fc='yellow', ec='grey', alpha=0.5))

        # Save the plot in the new folder with extracted timestamp
        plot_filename = get_next_filename(output_folder, "plot", "pdf", timestamp)
        plt.savefig(plot_filename, dpi=600, bbox_inches='tight')
        plt.close()

print("Plotting done...")
