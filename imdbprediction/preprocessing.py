import pandas as pd


movies = pd.read_csv('data/movie_metadata.csv')


def split_array(array, delimiter='|'):
    if isinstance(array, str):
        return array.split(delimiter)
    return []


def get_array_values(df, column):
    values = set()

    for index, row in df.iterrows():
        for value in split_array(row[column]):
            values.add(value)

    return values


def split_array_column(df, column, delimiter='|'):
    for value in get_array_values(df, column):
        df[value] = pd.Series([int(value in split_array(row[column])) for _, row in df.iterrows()])


split_array_column(movies, 'genres')

print(movies.head(1))
