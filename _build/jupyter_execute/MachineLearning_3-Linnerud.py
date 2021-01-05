#!/usr/bin/env python
# coding: utf-8

# # Linnerud

# In[1]:


from sklearn import datasets
ds = datasets.load_linnerud()
print(ds.DESCR)


# In[2]:


import pandas as pd
X = pd.DataFrame(ds.data,columns = ds.feature_names)
X.head(10)


# In[3]:


y = ds.target
y


# In[4]:


X.isnull().sum().sum()


# In[5]:


X.info()


# In[6]:


X.describe()


# In[7]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .2)
X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[8]:


y_train


# In[9]:


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)


# In[10]:


from sklearn.linear_model import LinearRegression
LinearRegressionObject = LinearRegression(normalize = True)
LinearRegressionObject.fit(X_train,y_train)


# In[11]:


from sklearn.metrics import mean_squared_error
y_pred = LinearRegressionObject.predict(X_test)
mean_squared_error(y_test,y_pred)


# In[12]:


from sklearn.metrics import r2_score
r2_score(y_test,y_pred)


# In[13]:


LinearRegressionObject.score(X_test,y_test)

