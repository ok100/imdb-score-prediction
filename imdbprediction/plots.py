import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from matplotlib.figure import Figure


def save_plot(plot, file_name):
    fig = plot.get_figure() if not isinstance(plot, Figure) else plot
    fig.savefig(file_name, bbox_inches='tight')


def plot_correlation(df, file_name):
    corr = df.corr()
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True
    cmap = sb.diverging_palette(220, 10, as_cmap=True)
    _, ax = plt.subplots(figsize=(11, 9))
    plot = sb.heatmap(corr, mask=mask, cmap=cmap, ax=ax, linewidths=0.5, cbar_kws={'shrink': .5})
    save_plot(plot, file_name)


sb.set(style='white')

movies = pd.read_csv('data/movie_metadata.csv')
num_data = movies.select_dtypes(include=[np.number])
cat_data = movies.select_dtypes(exclude=[np.number])


print(movies.describe())


# Densityplots
# for col in num_data.columns:
#     try:
#         _, ax = plt.subplots(figsize=(11, 9))
#         plot = sb.distplot(num_data[col].notnull(), ax=ax)
#         save_plot(plot, 'density_{}.png'.format(col))
#     except:
#         continue


# Boxplots
# for col in num_data.columns:
#     _, ax = plt.subplots(figsize=(11, 9))
#     plot = sb.boxplot(x=num_data[col], ax=ax)
#     save_plot(plot, 'box_{}.png'.format(col))



# # Histograms
# for col in cat_data.columns:
#     plot = cat_data[col].value_counts().plot(kind='bar')
#     save_plot(plot, 'hist_{}.png'.format(col))


# # Missing values
# sb.set_color_codes('pastel')
# plot = sb.barplot(x=movies.count(), y=movies.columns, color='b')
# sb.set_color_codes('muted')
# plot = sb.barplot(x=movies.isnull().sum(), y=movies.columns, color='b')
# save_plot(plot, 'null.png')


