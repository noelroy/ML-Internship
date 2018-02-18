
# coding: utf-8

# # Assignment 1

# In[15]:


import pandas as pd
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# ### 1. Using Pandas, load the dataset from https://www.kaggle.com/uciml/iris/data to a variable name iris

# In[16]:


iris = pd.read_csv("./iris-species/Iris.csv", index_col = 0)


# ### 2. Create a list named headers with all the column header names in the given order.

# In[17]:


headers = ["Id", "SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"]


# ### 3. Using the slice operation on headers, extract the column names with index 1 to 4 onto a list called features.

# In[18]:


features = headers[1:5]


# ### 4. Display the first five records of iris

# In[19]:


print(iris.head(5))


# ### 5. Make a scatterplot of the Iris features.

# In[20]:


scatter_matrix(iris, figsize=(8, 8))
plt.show()


# ### 6. What is the range of ‘SepalLengthCm’ in the dataset? What is the second largest value of ‘SepalLengthCm’ in the dataset?

# In[21]:


seplen = np.array(iris["SepalLengthCm"])
sorted = np.sort(seplen)
rang = max(sorted) - min(sorted)
print("Range {} [{} - {}]".format(rang, max(sorted), min(sorted)))
print("Second Largest {}".format(sorted[-2]))


# ### 7. Find the mean of all the values in SepalWidthCm using numpy

# In[22]:


sepwid = np.array(iris["SepalWidthCm"])
print(np.mean(sepwid))


# ### 8. Identify  ‘SepalLengthCm’  values less than 5. Create a new column named ‘Length’ , categorise each entry as ‘Small’ or ‘Large’, if less than 5.

# In[23]:


arr = np.empty([len(seplen),],dtype=object)
arr[seplen < 5] = "Small"
arr[seplen >= 5] = "Large"
iris["Length"] = arr
iris


# ### 9. Group dataFrame by the "Species" column. Make a histogram of the same.

# In[24]:


grouped = iris.groupby('Species')

# grouped.hist(figsize=(6,6))
# plt.show()

for x in features:
    grouped[x].hist(alpha=0.8,bins=20)
    plt.title(x)
    plt.legend(iris["Species"].unique())
    plt.show()

# iris.hist(by="Species",bins=6)
# plt.show()


# ### 10 .Find the deviation of length for ‘SepalLengthCm’ from the average

# In[25]:


print(np.std(seplen))


# ### 11 . Find correlation between columns and display columns with more than 70% percent correlation (either positive or negative).

# In[26]:


correl = iris.corr(method='spearman')
print("Correlation")
print(correl)

columns = []

for x in features:
    for y in features:
        if (abs(correl[x][y]) > 0.7) and (x != y):
            columns.append(x)
print("Columns")
print(np.unique(columns))


# ### 12. Impute missing values if present using mean of the dataset.

# In[27]:


for x in features:
    iris[x].fillna(iris[x].mean(), inplace=True)


# ### 13. Save the current dataFrame out to a new csv file.

# In[28]:


iris.to_csv("newdata.csv")

