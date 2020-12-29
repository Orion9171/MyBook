#!/usr/bin/env python
# coding: utf-8

# # Iris_Classification 

# In[1]:


from sklearn import datasets
ds = datasets.load_iris()
print(ds.DESCR)


# In[2]:


import pandas as pd
X = pd.DataFrame(ds.data,columns = ds.feature_names)
X


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
X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[8]:


y_train


# In[9]:


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)


# In[10]:


from sklearn import neighbors
clf = neighbors.KNeighborsClassifier(n_neighbors = 5)
clf.fit(X_train_std,y_train)


# In[11]:


y_pred = clf.predict(X_test_std)
y_pred


# In[12]:


y_test == y_pred


# In[13]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)


# In[14]:


clf2 = neighbors.KNeighborsClassifier(n_neighbors = 11)
clf2.fit(X_train_std,y_train)


# In[15]:


y_pred = clf2.predict(X_test_std)
accuracy_score(y_test,y_pred)


# In[16]:


from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

