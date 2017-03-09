import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sb.set(style='white')
movies = pd.read_csv('data/movie_metadata.csv')


# Missing values
_, ax = plt.subplots(figsize=(11, 9))

sb.set_color_codes('pastel')
plot = sb.barplot(x=movies.count(), y=movies.columns, color='b')

sb.set_color_codes('muted')
plot = sb.barplot(x=movies.isnull().sum(), y=movies.columns, color='b')

fig = plot.get_figure()
fig.savefig('null.png', bbox_inches='tight')


# Correlation
corr = movies.corr()

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

_, ax = plt.subplots(figsize=(11, 9))

cmap = sb.diverging_palette(220, 10, as_cmap=True)

plot = sb.heatmap(corr, mask=mask, cmap=cmap, ax=ax, linewidths=0.5, cbar_kws={'shrink': .5})
fig = plot.get_figure()
fig.savefig('corr.png', bbox_inches='tight')
