#!/usr/bin/env python
# coding: utf-8

# # Lab 1 -- Regression

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


X.info()


# In[5]:


X.describe()


# In[6]:


X.isnull().sum().sum()


# In[7]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = .2)
X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[8]:


y_train


# In[9]:


from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
#data standarlizing
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)
#algorithm define & using algorithm to train the data
from sklearn.linear_model import LinearRegression
LinearRegressionObject = LinearRegression(normalize = True)
LinearRegressionObject.fit(X_train,y_train)
print('Wx:',LinearRegressionObject.coef_)
print('b:',LinearRegressionObject.intercept_)
from sklearn.metrics import mean_squared_error,r2_score
y_pred = LinearRegressionObject.predict(X_test) #use X_test for prediction
#using the chosen algorithm to calculate MSE & R2 score(效能指標)
print('MSE:',mean_squared_error(y_test,y_pred))
print('R2:',r2_score(y_test,y_pred))


# In[10]:


LinearRegressionObject.score(X_test,y_test)


# In[11]:


#計算RMSE記得開根號
print('RMSE:',mean_squared_error(y_test,y_pred)**.5)


# # Scikit-Learn二次迴歸求迴歸方程式

# In[12]:


#2次迴歸
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 2)
X2 = poly.fit_transform(X)


# In[13]:


#再次切割資料
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X2,y,test_size = .2)
X_train.shape,X_test.shape,y_train.shape,y_test.shape


# In[14]:


#再次訓練
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
#data standarlizing
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)
#algorithm define & using algorithm to train the data
from sklearn.linear_model import LinearRegression
LinearRegressionObject = LinearRegression(normalize = True)
LinearRegressionObject.fit(X_train,y_train)


# In[15]:


LinearRegressionObject.score(X_test,y_test)


# # Scikit-Learn三次迴歸求迴歸方程式

# In[16]:


#3次迴歸
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 3)
X3 = poly.fit_transform(X)
#再次切割資料
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X3,y,test_size = .2)
X_train.shape,X_test.shape,y_train.shape,y_test.shape
#再次訓練
from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
#data standarlizing
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)
#algorithm define & using algorithm to train the data
from sklearn.linear_model import LinearRegression
LinearRegressionObject = LinearRegression(normalize = True)
LinearRegressionObject.fit(X_train,y_train)
LinearRegressionObject.score(X_test,y_test)

