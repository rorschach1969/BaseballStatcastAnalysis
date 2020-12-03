# Let's get some runs
import matplotlib.pyplot as plt
import pandas as pd
import os
import platform
import numpy as np
from pybaseball import batting_stats_bref
from pybaseball import pitching_stats
from pybaseball import playerid_lookup
from pathlib import Path, PureWindowsPath


plt.style.use('ggplot')

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 4000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', -1)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')

def read_path(name):
    osType = platform.platform()
    dir_path = os.path.dirname(os.path.realpath(__file__)) + '/' + name
    if osType == 'Windows':
        dir_path = PureWindowsPath(dir_path)
    return dir_path

def read_data(name):
    return pd.read_csv(read_path(name))

def update_stats_csv(data, fileName, type):
    if type == 'csv':
        data.to_csv(read_path(fileName))
    else:
        data.to_excel(read_path(fileName))

def compute_histogram_bins(data, desired_bin_size):
    min_val = np.min(data)
    max_val = np.max(data)
    min_boundary = -1.0 * (min_val % desired_bin_size - min_val)
    max_boundary = max_val - max_val % desired_bin_size + desired_bin_size
    n_bins = int((max_boundary - min_boundary) / desired_bin_size) + 1
    bins = np.linspace(min_boundary, max_boundary, n_bins)
    return bins



#update_stats_csv(pitching_stats(2012,2018, 'al', 50, 1), 'pitching.csv', 'csv')
#bins = np.linspace(0.0,8.0, num=32)

data = read_data('pitching.csv')
bins = compute_histogram_bins(data['ERA'], 0.25000000000)
data['ERA'].plot.hist(bins=bins, histtype='bar', ec='black')
#setting the rows to be by name or by any column. Soon to happen during app dev portion
#stats = data.set_index(['Name'])
plt.xticks(np.arange(0, 8.5, step=0.25), rotation=90)
plt.title('Pitcher ERA from 2012-2018')
plt.xlabel('ERA')
#pitcher = stats.loc[stats.index.isin(['Justin Verlander', 'Chris Sale'])]
#stats['ERA'].plot.hist()
#pitcher[['ERA', 'Season']].plot()
#plt.show()
#categories = data.columns.tolist()
#print_full(categories)

#print(data[['ERA', 'W', 'Name']])
plt.show()
#average = data.mean(axis=0)
#print(average)




