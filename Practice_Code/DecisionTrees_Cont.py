#!/usr/bin/env python
# coding: utf-8

# # Ensembles

# In[2]:


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.externals.six import StringIO
import subprocess


# In[3]:


from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.externals.six import StringIO
import subprocess


# In[11]:


np.random.seed(1234)

mod1=np.random.rand(5000)
mod2 = np.random.rand(5000)
mod3 = np.random.rand(5000)
mod4 = np.random.rand(5000)
mod5 = np.random.rand(5000)


# In[12]:



# each model independently predicts 1 (the "correct response") if random number was at least 0.3
preds1 = np.where(mod1 > 0.3, 1, 0)
preds2 = np.where(mod2 > 0.3, 1, 0)
preds3 = np.where(mod3 > 0.3, 1, 0)
preds4 = np.where(mod4 > 0.3, 1, 0)
preds5 = np.where(mod5 > 0.3, 1, 0)


# In[13]:


print(preds1[:20])
print(preds2[:20])
print(preds3[:20])
print(preds4[:20])
print(preds5[:20])


# In[15]:


# average the predictions and then round to 0 or 1
ensemble_preds = np.round((preds1 + preds2 + preds3 + preds4 + preds5)/5.0).astype(int)

# print the ensemble's first 20 predictions
print(ensemble_preds[:20])


# In[16]:


# how accurate was each individual model?
print(preds1.mean())
print(preds2.mean())
print(preds3.mean())
print(preds4.mean())
print(preds5.mean())


# In[17]:


# how accurate was the ensemble?
print(ensemble_preds.mean())


# In[18]:


### Bagging


# In[19]:


# set a seed for reproducibility
np.random.seed(20)

# create an array of 1 through 30
nums = np.arange(1, 30)
print("The original array:",nums)

# sample that array 15 times with replacement
print("The 15 samples:",np.random.choice(a=nums, size=15, replace=True))


# In[20]:


### Manually implementing Bagged regression Trees

np.random.seed(1234)

samples=[np.random.choice(a=X_train.shape[0],size=X_train.shape[0],replace=True) for _ in range(1,11)]


# In[ ]:




