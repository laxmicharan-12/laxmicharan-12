#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pandas import read_csv
import seaborn as sns 
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2,f_regression,f_classif
dataframe=sns.load_dataset('tips')
dataframe


# In[6]:


df=sns.load_dataset("tips")
df


# In[7]:


df


# In[8]:


from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()


# In[9]:


df['smoker']=lb.fit_transform(df['smoker'])
df['sex']=lb.fit_transform(df['sex'])
df['time']=lb.fit_transform(df['time'])
df['day']=lb.fit_transform(df['day'])


# In[10]:


df


# In[ ]:




