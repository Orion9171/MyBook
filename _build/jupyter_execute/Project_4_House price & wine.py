#!/usr/bin/env python
# coding: utf-8

# # Lab 1 - LinearRegressionPractice

# In[1]:


from sklearn import datasets
ds = datasets.load_boston()
print(ds.DESCR)


# In[2]:


import pandas as pd
X = pd.DataFrame(ds.data,columns = ds.feature_names)
X.head(10)


# In[3]:


y = ds.target
y


# In[4]:


X.info()


# In[5]:


X.isnull().sum().sum()


# In[6]:


X.describe()


# In[7]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .2)


# In[8]:


X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[9]:


y_train


# In[10]:


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)


# In[11]:


X_test_std = scaler.transform(X_test)


# In[12]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize = True)


# In[13]:


lr.fit(X_train,y_train)


# In[14]:


from sklearn.metrics import mean_squared_error
y_pred = lr.predict(X_test)
mean_squared_error(y_test,y_pred)


# In[15]:


from sklearn.metrics import r2_score
r2_score(y_test,y_pred)


# # Lab 2 - ClassificationPractice

# In[16]:


from sklearn import datasets
ds = datasets.load_wine()
print(ds.DESCR)


# In[17]:


import pandas as pd
X = pd.DataFrame(ds.data,columns = ds.feature_names)
X.head(10)
X


# In[18]:


y = ds.target
y


# In[19]:


X.info()


# In[20]:


X.isnull().sum().sum()


# In[21]:


X.describe()


# In[22]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .2)


# In[23]:


X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[24]:


y_train


# In[25]:


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)


# In[26]:


X_test_std = scaler.transform(X_test)


# In[27]:


from sklearn import neighbors
clf = neighbors.KNeighborsClassifier(n_neighbors = 5)
clf.fit(X_train_std,y_train)


# In[28]:


y_pred = clf.predict(X_test_std)
y_pred


# In[29]:


y_test == y_pred


# In[30]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[31]:


clf2 = neighbors.KNeighborsClassifier(n_neighbors = 11)
clf2.fit(X_train_std,y_train)


# In[32]:


y_pred = clf2.predict(X_test_std)
accuracy_score(y_test,y_pred)


# In[33]:


from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

