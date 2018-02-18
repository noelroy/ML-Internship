
# coding: utf-8

# # Assignment 2

# In[30]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### 1. Read and merge the dataset into single dataframe

# In[31]:


ign = pd.read_csv("./ign/ign.csv", index_col="id")
ign_score = pd.read_csv("./ign/ign_score.csv", index_col="id")
# ign_new = pd.concat([ign, ign_score], axis=1)
# ign_new = pd.merge(ign, ign_score, left_index=True, right_index=True)
ign_new = ign.join(ign_score)


# ### 2. Provide the names of 10 movies rated highest.

# In[32]:


score_sorted = ign_new.sort_values(by="score", ascending=False)
print(score_sorted["title"].unique()[:10])


# ### 3. Rank the movie names by their highest average rating scores.

# In[33]:


score_average = ign_new.groupby('title')['score'].transform('mean')
score_rank = score_average.rank(method ='dense', ascending=False)
ign_new = ign_new.assign(Rank=score_rank)
ign_new


# ### 4. Plot movie scores across each genre.

# In[37]:


ign_new.hist(by="genre", column="score", figsize=(30,40),grid =True)
plt.show()


# ### 5. Find the group that provides the highest average movie ratings when split into genre groups.

# In[35]:


# genre_means = ign_new[['genre','score']].groupby('genre').mean()
score_average = ign_new.groupby('genre')[['score']].mean()
sorted_score = score_average.sort_values(by='score',ascending=False)
print(sorted_score.head(1).index.values)


# ### 6. Provide a table with the average rating of a movie by each genre group along with the movie title.

# In[36]:


table = pd.pivot_table(ign_new, values='score', index=['genre', 'title'])
table

