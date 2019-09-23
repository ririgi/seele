import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append("../")

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk
import matplotlib as mpl
mpl.use('tKagg')
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')
style.use('bmh')
plt.tight_layout()

def distrib_plot(file, content_type):
	df = pd.read_csv(file)
	print(df.head())
	for col in ['RECENCY', 'FREQUENCY', 'ENGAGEMENT']:
		plot = sns.distplot(a = df[col].values, kde = False)
		plot.set_xlabel(col)
		plt.savefig('visualization/'+content_type+col+'.png', dpi = 600)
		plt.clf()

def scatter_plot(file, content_type):
	df = pd.read_csv(file)
	print(df.head())
	plot = sns.regplot('RECENCY', 'FREQUENCY', data = df, fit_reg = False)
	plot.set_xlabel('RECENCY')
	plot.set_ylabel('FREQUENCY')
	plt.savefig('visualization/scatter/'+content_type+'rf.png', dpi = 600)
	plt.clf()

	plot = sns.regplot('RECENCY', 'ENGAGEMENT', data = df, fit_reg = False)
	plot.set_xlabel('RECENCY')
	plot.set_ylabel('FREQUENCY')
	plt.savefig('visualization/scatter/'+content_type+'re.png', dpi = 600)
	plt.clf()

	plot = sns.regplot('FREQUENCY', 'ENGAGEMENT', data = df, fit_reg = False)
	plot.set_xlabel('FREQUENCY')
	plot.set_ylabel('ENGAGEMENT')
	plt.savefig('visualization/scatter/'+content_type+'fe.png', dpi = 600)
	plt.clf()

if __name__ == '__main__':
	distrib_plot('results/channel2.csv', 'channel2')
	distrib_plot('results/origshow.csv', 'origshow')
	distrib_plot('results/origmovie.csv', 'origmovie')
	distrib_plot('results/movie.csv', 'movie')

	scatter_plot('results/channel2.csv', 'channel2')
	scatter_plot('results/origshow.csv', 'origshow')
	scatter_plot('results/origmovie.csv', 'origmovie')
	scatter_plot('results/movie.csv', 'movie')