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

raw_data = pd.DataFrame.from_csv('data/data_in_days.csv')

# Create bins of BIN_SIZE days from 0 to last day. (Need to add BIN_SIZE days
# to ensure we get a bin with the last data points in it.)
BIN_SIZE = 90
last_day = raw_data.iloc[-1]['sustainment']

day_counts = raw_data.groupby('sustainment', as_index = False).count()

total_projects = day_counts['name'].sum()
zero_day = day_counts['name'][0]
zero_day_p = (float(zero_day) / float(total_projects)) * 100.0
under_seven = 0
for d in range(0, 7):
    under_seven += day_counts['name'][d]
under_seven_p = (float(under_seven) / float(total_projects)) * 100.0

print "Total number of projects: %d" % total_projects
print "Number of projects S = 0: %d (%f%%)" % (zero_day, zero_day_p)
print "Number of projects S < 7: %d (%f%%)" % (under_seven, under_seven_p)

bins = range(0, (last_day + BIN_SIZE), BIN_SIZE)

data = [[], [], []]
for s in [0, 1, 2]:
    day_counts['bins'] = pd.cut(day_counts.sustainment.iloc[s:], bins, right = False, labels = bins[:-1])

    data[s] = [day_counts[['name', 'bins']].groupby('bins').sum().dropna(), s]

for d in data:
    fig, ax = plt.subplots()
    ax = d[0].plot(legend = None)

    for item in ['top', 'right']:
        ax.spines[item].set_visible(False)

    ax.set_xlabel('Sustainment (days)')
    ax.set_ylabel('Number of projects')
    fig.set_size_inches(6, 3)
    fig.tight_layout()

    name = 'output/binned-plot-%d.pdf' % d[1]
    plt.savefig(name)
