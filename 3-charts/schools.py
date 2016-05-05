import pandas as pd
import matplotlib.pyplot as plt
%matplotlib
from os.path import join
fname = join('matplotlibsampler', 'data', 'schools', 'frpm-2014.csv')

df = pd.read_csv(fname)
plt.scatter(df['enrollment_k12'], df['adjusted_pct_eligible_free_k12'])
