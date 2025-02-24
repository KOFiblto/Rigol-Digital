import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt


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





df = pd.read_csv('channels.csv', header=None)
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
#ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2)
plt.legend()

#tick_spacing = 50
#ax.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))


# add text box for the statistics
stats = (f'$u_e$ = {np.max(ue):.2f}' + ' \\unit{\\mV}' + '\n'
         f'$u_a$ = {np.max(ua):.2f}' + ' \\unit{\\mV}')

plt.gcf().text(1.025, 0.9, stats, transform=ax.transAxes, horizontalalignment='left', fontsize=12, \
               bbox = dict(boxstyle='round', fc='yellow', ec='grey', alpha=0.5))
    
###plt.show() #does not work with pgf backend !
plt.savefig('BJT_ceAmp_acAnalysis.pdf', dpi=600, bbox_inches='tight')
plt.close()

print("plotting done...")
