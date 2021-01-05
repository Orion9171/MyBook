#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
h=np.around(np.random.normal(loc=175,scale=10,size=5000),1)
w=np.around(np.random.normal(loc=60,scale=15,size=5000),1)
print(h)
print('----------')
print(w)
print('----------')


# In[2]:


m_height=np.max(h,axis=None)
l_height=np.min(h,axis=None)
m_weight=np.max(w,axis=None)
l_weight=np.min(w,axis=None)
print('身高範圍:')
print('最高身高:',m_height)
print('最矮身高',l_height)
print('-------------------')
print('體重範圍:')
print('最肥體重:',m_weight)
print('最輕體重:',l_weight)


# In[3]:


#average calculation
avr_height=np.around(np.mean(h,axis=None))
avr_weight=np.around(np.mean(w,axis=None))
print('平均身高:',avr_height)
print('平均體重:',avr_weight)


# In[4]:


#medium number
m_h=np.median(h,axis=None)
m_w=np.median(w,axis=None)
print('身高中位數:',m_h)
print('體重中位數:',m_w)


# In[5]:


#standard division
s_h=np.around(np.std(h,axis=None))
s_w=np.around(np.std(w,axis=None))
print('身高標準差:',s_h)
print('體重標準差:',s_w)


# In[6]:


h_w=np.corrcoef(h,w)
print(h_w)


# In[ ]:





# In[ ]:




