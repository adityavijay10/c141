import pandas as pd

df=pd.read_csv('movies.csv')
print(df.shape)
del df['id']
del df['budget']
del df['index']
del df['title_x']
del df['title_y']
del df['spoken_languages']
# print(df.shape)
df.to_csv('movies.csv')
