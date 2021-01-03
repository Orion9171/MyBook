#!/usr/bin/env python
# coding: utf-8

# # matrix_practice

# In[1]:


import numpy as np
a = np.array([[2,4],
              [6,2]])
b = np.array([18,34])
c = np.linalg.inv(a.T@a)@a.T@b
print(c)


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (12,8))
ax = plt.axes(projection = '3d')
X = a
y = b
X1 = X[:,0].reshape(X.shape[0])
X2 = X[:,1].reshape(X.shape[0])
ax.scatter3D(X1,X2,y,cmap = 'hsv',marker = 'o',s = [160,160])
X1 = np.linspace(2,8,50)
X2 = np.linspace(2,8,50)
x_surf,y_surf = np.meshgrid(X1,X2)
z_surf = x_surf * 5 + y_surf * 2
from matplotlib import cm
ax.plot_surface(x_surf,y_surf,z_surf,cmap = cm.hot)
plt.show()

