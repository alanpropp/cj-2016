import pandas as pd
import matplotlib.pyplot as plt
%matplotlib
from os.path import join
fname = join('matplotlibsampler', 'data', 'stocks')
files = ['AAPL.csv', 'AMZN.csv', 'FB.csv', 'GOOG.csv', 'MSFT.csv', 'YHOO.csv']
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
x = 0
for f in files:
	df = pd.read_csv(join(fname, f), parse_dates=['Date'])
	#fig, ax = plt.subplots()
	plt.plot(df['Date'], df['Adj Close'], color = colors[x], label = f[0:-4])
	x+=1

legend = plt.legend()