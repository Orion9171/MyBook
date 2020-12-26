#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
#新竹下星期天氣
#上課工具總複習
import matplotlib.pyplot as plt
t=[33,33,33,35,35,35,34]
w=range(1,8)
plt.plot(w,t,'co-')
plt.axis((1,7,0,50))
plt.figure(num=1,facecolor='blue',edgecolor='red',figsize=(8,5),linewidth=10)
plt.grid(which='major',axis='both')
plt.xticks(w,['mon','tues','wed','thurs','fri','sat','sun'])
plt.title('新竹一星期均溫')
plt.xlabel('Days')
plt.ylabel('temperature')
plt.fill_between(w,t,color='red')
import numpy as np
avr=np.around(np.mean(t),1)
print('新竹下星期平均溫:',avr)


# In[2]:


#salary
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
normal_salary=[27583,27555,26492,29441,24973,27499,26421,29686,27156,26771,25499,26571,28029,27624,30176,31058,29404,27492
        ,27092,26941,28207,28825,27307,27502,26676,26621,24789,26759,29928,29517,32492,28628,28467,32777,26276,25981,22316,34328,24754,
        28537,26853,27702,29885,29653,27005,26066,27628,26758,27682,25679,28294,31711,27439,25416,26491,32800,33325,
        35821,28181,27548,38151,27932,26304,27024,26765,28832,27956,25540,26941,28626,29984,29440,32044,36354,25470,
        28820,32522,30741,29201,36384,29176,28092,29266,27383,29052,32467,28191,28852,29854,28025,28838,26941,26243
        ,28168,25263,25426,25607,26804,26062,26374,26392,27739,26006,27635,25896,24614,24701,23187,25841]
data_s=pd.Series(normal_salary)
print(data_s.describe(percentiles=[0.25,0.50 ,0.75,0.80,0.90 ]))
x=range(1,len(normal_salary)+1)
plt.plot(x,normal_salary,'-')
plt.figure(num=1,figsize=(20,10))
plt.xlabel('Range',fontsize=16)
plt.ylabel('Salary',fontsize=16)
plt.title('台灣經常性薪資整理圖',fontsize=18,color='b')
plt.grid(which='major',axis='y',color='black')
high_s=np.max(normal_salary)
low_s=np.min(normal_salary)
mid_s=np.median(normal_salary)
avr=np.around(np.mean(normal_salary),1)
value1=np.around(26491.000000,1)
value2=np.around(27624.000000,1)
value3=np.around(29201.000000,1)
value4=np.around(29571.400000,1)
value5=np.around(32128.600000,1)
print('經常性薪資最大值:',high_s)
print('經常性薪資最小值:',low_s)
print('經常性薪資中位數:',mid_s)
print('經常性薪資平均值:',avr)
print('經常性薪資於90%區間的值:',value5)
print('經常性薪資於80%區間的值:',value4)
print('經常性薪資於75%區間的值:',value3)
print('經常性薪資於50%區間的值:',value2)
print('經常性薪資於25%區間的值:',value1)
plt.show()


# In[ ]:




