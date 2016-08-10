#------------------------------------------------------------------------------
# Copyright (c) 2016, The University of Manchester, UK.
#
# BSD licenced. See LICENCE for details.
#
# Authors: Robert Haines
#------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.DataFrame.from_csv('data/data_in_days.csv', header=None)
counts = raw_data.groupby(2).count()
data = [[counts, '0'], [counts[1:], '1'], [counts[2:], '2']]

for d in data:
    fig, ax = plt.subplots()
    ax.plot(d[0])

    for item in [fig, ax]:
        item.patch.set_visible(False)

    for item in ['top', 'right', 'bottom', 'left']:
        ax.spines[item].set_visible(False)

    ax.set_xlabel('Sustainability (days)')
    ax.set_ylabel('Number of projects')
    ax.set_xlim([0, 2800])
    fig.set_size_inches(6, 3)
    fig.tight_layout()

    name = 'output/plot-' + d[1] + '.pdf'
    plt.savefig(name)
