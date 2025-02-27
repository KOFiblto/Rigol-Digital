import os
import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import re  # To extract the timestamp from the file name

############# Plotting ########
# Disable LaTeX rendering
mpl.rcParams.update({
    "text.usetex": False  # Disable LaTeX rendering
})

def get_next_filename(folder: str, prefix: str, extension: str, timestamp: str) -> str:
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"{prefix}_{timestamp}.{extension}")
    return filename

# Loop through files in the channels folder (one level up)
channels_folder = os.path.join(os.getcwd(), '..', 'channels')
output_folder = os.path.join(os.getcwd(), '..', 'plots')

# Check if channels folder exists
if not os.path.exists(channels_folder):
    print(f"Channels folder not found: Rigol-Digital/channels. Please either manually create it or get csv files by running the program")
    exit()

for filename in os.listdir(channels_folder):
    if filename.endswith('.csv'):  # Check if it's a CSV file
        file_path = os.path.join(channels_folder, filename)
        
        # Extract timestamp from the filename (assuming format: channel_Y-M-D_H-M-S.csv)
        match = re.match(r'channel_(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})\.csv', filename)
        if match:
            timestamp = match.group(1)
        else:
            continue  # Skip files that don't match the expected format
        
        df = pd.read_csv(file_path, header=None, delimiter=',')

        if df.shape[1] < 2:
            print(f"Skipping {filename}: Not enough columns (found {df.shape[1]}).")
            continue
        
        t = df[0] * 1E3
        ue = df[1] * 1E3
        ua = df[2] * 1E3 if df.shape[1] > 2 else np.zeros_like(ue)  # Handle missing third column
        
        plt.plot(t, ue, label="$u_e$", color='orange')
        if df.shape[1] > 2:
            plt.plot(t, ua, label="$u_a$", color='blue')

        ax = plt.gca()
        ax.set_xlabel('Time (ms)', labelpad=5)
        ax.set_ylabel("Voltage (mV)", labelpad=0)
        
        # mark peak voltages with horizontal lines
        ax.axhline(np.max(ue), linestyle='--', linewidth=1, color='orange')
        if df.shape[1] > 2:
            ax.axhline(np.max(ua), linestyle='--', linewidth=1, color='blue')
        
        plt.legend()
        
        # add text box for the statistics
        stats = f'$u_e$ = {np.max(ue):.2f} mV'
        if df.shape[1] > 2:
            stats += f'\n$u_a$ = {np.max(ua):.2f} mV'        
        plt.gcf().text(1.025, 0.9, stats, transform=ax.transAxes, horizontalalignment='left', fontsize=12,
                       bbox=dict(boxstyle='round', fc='yellow', ec='grey', alpha=0.5))

        # Save the plot in the new folder with extracted timestamp
        plot_filename = get_next_filename(output_folder, "plot", "pdf", timestamp)
        plt.savefig(plot_filename, dpi=600, bbox_inches='tight')
        plt.close()

print("Plotting done...")
