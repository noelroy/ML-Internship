
# coding: utf-8

# # Assignment 3

# In[1]:


import numpy as np


# ### 1. Create a function which creates an n×n array with (i,j)-entry equal to i+j.

# In[2]:


def nparr(n):
    arr = np.zeros((n, n))
    for x in range(1,n):
        arr[x:n] = arr[x:n] + 1
        arr[:,x:n] = arr[:,x:n] + 1
    return arr
print(nparr(5))


# ### 2. Create a numpy array which contains odd numbers below 20. Arrange it to a 2x5 matrix. Compute the log of each element

# In[3]:


oddns = np.arange(1,20,2)
reshaped = oddns.reshape((2,5))
print("Reshaped Array")
print(reshaped)
logns = np.log(reshaped)
print("Log of Array")
print(logns)


# ### 3. Create a function which creates an n×n random array. Subtract the average of each row of the matrix 

# In[4]:


def avg (a):
    return a-np.average(a)

def nprand(n):
    return np.random.rand(n,n)

arr = nprand(3)
print("Random Array")
print(arr)
new = np.apply_along_axis(avg, 1, arr)
print("Avg Array")
print(new)


# ### 4. Create a function which creates an n×n random array. Write a program to find the nearest value from a given value in the array

# In[5]:


def nprand(n):
    return np.random.rand(n,n)

n = 4
val = 0.5

arr = nprand(n)
print("Random Array")
print(arr)
index = np.argmin([np.abs(arr-val)])
print("Nearest Value")
print(arr.flat[index])


# ### 5. Write a function to check if two random arrays are equal or not

# In[6]:


def check_equal(a,b):
    return np.array_equal(a,b)

print(check_equal([1, 2], [1, 2]))
print(check_equal([1, 2], [1, 2, 3]))
print(check_equal([1, 2], [1, 4]))


# ### 6. Create a function to get the n largest values of an array

# In[7]:


def nlarge(arr,n):
    arr = np.sort(arr)[::-1]
    return arr[:n]

n = 4

arr = np.random.randint(9,size=10)
print("Random array")
print(arr)
print(nlarge(arr, n))

