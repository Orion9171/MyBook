#!/usr/bin/env python
# coding: utf-8

# # MatrixEquation

# In[1]:


from sklearn import datasets
ds = datasets.load_boston()
print(ds.DESCR)


# In[2]:


import pandas as pd
X = pd.DataFrame(ds.data,columns = ds.feature_names)
X


# In[3]:


y = ds.target
y


# In[4]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .2)
X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[5]:


X.shape


# In[6]:


import numpy as np
b = np.ones((X_train.shape[0],1))
b.shape


# In[7]:


X_train = np.hstack((X_train,b))


# In[8]:


#c = np.linalg.inv(a.T@a)@a.T@b
W = np.linalg.inv(X_train.T@X_train)@X_train.T@y_train


# In[9]:


W


# In[10]:


#algorithm define & using algorithm to train the data
from sklearn.linear_model import LinearRegression
LinearRegressionObject = LinearRegression(normalize = True)
LinearRegressionObject.fit(X_train,y_train)


# In[11]:


b = np.ones((X_test.shape[0],1))
b.shape


# In[12]:


X_test = np.hstack((X_test,b))


# In[13]:


SSE = ((X_test@W-y_test)**2).sum()
MSE = SSE/y_test.shape[0]
RMSE = MSE ** (1/2)
RMSE


# In[14]:


y_mean = y.ravel().mean()
SST = ((y - y_mean)**2).sum()
R2 = 1 - (SSE/SST)
R2

