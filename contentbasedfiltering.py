import numpy as  np
import pandas as pd

df=pd.read_csv('final.csv')
df=df[df['soup'].notna()]
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

count=CountVectorizer(stop_words='english')
countMatrix=count.fit_transform(df['soup'])

cosine_sim=cosine_similarity(countMatrix,countMatrix)

df1=df.reset_index()
indices=pd.Series(df.index,index=df['original_title'])

def get_recomdations(title):
  idx=indices[title]
  sim_scores=list(enumerate(cosine_sim[idx]))
  sim_scores=sorted(sim_scores,key=lambda x:x[1],reverse=True)
  sim_scores=sim_scores[1:11]
  movie_indices=[i[0] for i in sim_scores]
  return(df['original_title','imdb_link','release_date','vote_average','overview'].iloc[movie_indices]).values.tolist()
