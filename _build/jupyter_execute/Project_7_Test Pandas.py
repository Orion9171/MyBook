#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd
fruits=["蘋果", "橘子", "梨子", "櫻桃"]
s1=pd.Series(fruits)
print(type(s1))
print(s1)
print(s1.index)
print(s1.values)
print()
quantities=[15, 33, 45, 55]
s2=pd.Series(quantities,fruits)
print(type(s2))
print(s2)
print(s2.index)
print(s2.values)
print(s2['蘋果'])


# In[3]:


import pandas as pd
fruits=["蘋果", "橘子", "梨子", "櫻桃"]
quantities=[15, 33, 45, 55]
s3=pd.Series(quantities)
print(type(s3))
print(s3)
print(s3.index)
print(s3.values)
print()
dict4={"蘋果":15, "橘子":33, "梨子":45, "櫻桃":55}
s4=pd.Series(dict4)
print(type(s4))
print(s4)
print(s4.index)
print(s4.values)


# In[4]:


import pandas as pd
quantities = [15, 33, 45, 55]
s5 = pd.Series(quantities)
print(s5.count( ))
print(s5.median( ))
print(s5.mean( ))
print(s5.min( ))
print(s5.max( ))
print("---------")
print(s5.describe( ))
print(s5.var( ))
print(s5.std ( ))
print(s5.apply(lambda x:x**2))


# In[5]:


import pandas as pd
data1={'name':['Tom','Jack','Stella','Ricky'],'age':[28,34,29,42],'gender':['m','m','f','m']}
df1=pd.DataFrame(data1)
print(df1)
df2=pd.DataFrame(data1,index=['emp1','emp2','emp3','emp4'])
print(df2)
df3=pd.DataFrame(data1,index=range(1,5),columns=(['name','gender']))
print(df3)
df4=pd.DataFrame(data1,index=range(1,5),columns=(['name','age']))
print(df4)


# In[6]:


import pandas as pd
data2=[{'Name':'Tom', 'Age': 28, 'Gender':'M'},
      {'Name':'Jack', 'Age': 34, 'Gender':'M'},
      {'Name':'Stella', 'Age': 29, 'Gender':'F'},
      {'Name':'Ricky', 'Age': 42, 'Gender':'M'}]
df1=pd.DataFrame(data2)
print(df1)
df2=pd.DataFrame(data2,index=['emp1','emp2','emp3','emp4'],columns=(['Name','Age','Gender']))
print(df2)
df3=pd.DataFrame(data2,index=range(1,5),columns=(['Name','Gender']))
print(df3)
df4=pd.DataFrame(data2,index=range(1,5),columns=(['Name','Age']))
print(df4)


# In[7]:


import pandas as pd
data3=[['Tom',28,'m'],['Jack',34,'m'],['Stella',29,'f'],['Ricky',42,'m']]
df1=pd.DataFrame(data3)
print(df1)
df2=pd.DataFrame(data3,index=range(1,5),columns=('name','age','gender'))
print(df2)


# In[8]:


import pandas as pd
import numpy as np
data4=np.array([['Tom', 28, 'M'],['Jack',34,'M'],['Stella',29,'F'],['Ricky',42,'M']])
df1=pd.DataFrame(data4)
print(df1)
df2=pd.DataFrame(data4,index=range(1,5),columns=['Name','Age','Gender'])
print(df2)


# In[9]:


import pandas as pd
cindex=range(1,5)
data5={'Name' : pd.Series(['Tom', 'Jack', 'Stella', 'Ricky'],index=cindex),
                        'Age' : pd.Series([28,34,29,42],index=cindex),
                        'Gender' : pd.Series(['M', 'M', 'F', 'M'],index=cindex)}
df1 = pd.DataFrame(data5,index=cindex)
print(df1)
data6 = [pd.Series(['Tom', 28, 'M'],index=['name','age','gender']),
         pd.Series(['Jack', 34, 'M'],index=['name','age','gender']),
         pd.Series(['Stella', 29, 'F'],index=['name','age','gender']),
         pd.Series(['Ricky', 42, 'M'],index=['name','age','gender'])]
df2 = pd.DataFrame(data6,index=range(1,5))
print(df2)


# In[10]:


rindex=range(1,5)
s1=pd.Series(['Tom','Jack','Stella','Ricky'],index=rindex)
s2=pd.Series([28,34,29,42],index=rindex)
s3=pd.Series(['M','M','F','M'],index=rindex)
data7={'name':s1,'age':s2,'gender':s3}
data8=pd.DataFrame(data7,index=rindex)
print(data8)


# In[11]:


import pandas as pd
data = {"country":["Brazil","Russia","India","China","SouthAfrica"],
        "population":[200,144,1252,1357,55],
        "area":[8515767,17098242,3287590,9596961,1221037],
        "capital":["Brasilia","Moscow","NewDelhi","Beijing","Pretoria"]}
df=pd.DataFrame(data,index=['BR','RU','IN','CH','SA'])
print(df)
df.to_html('brics.html')
df.to_csv('brics.csv')
df.to_csv('brics2.csv',header=False)
df.to_json('brics.json')


# In[12]:


import pandas as pd
data = {"name": ["中正區", "板橋區", "桃園區", "北屯區", "安南區", "三民區", "大安區", "永和區", "八德區", "前鎮區", "鳳山區", "信義區", "新店區"],
        "population": [159598, 551452, 441287, 275207, 192327, 343203, 309835, 222531, 198473, 189623, 359125, 225561, 302070],
        "city": ["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市", "台北市", "新北市", "桃園市", "高雄市", "高雄市", "台北市", "新北市"]}
rows = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh","eigth", "ninth", "tenth", "eleventh", "twelvth", "thirteenth"]
df2=pd.DataFrame(data,index=rows)
print(df2)
df2.to_html('area.html')
df2.to_csv('area.csv')
df2.to_json('area.json',force_ascii=False)


# In[13]:


import pandas as pd
df1=pd.read_csv('brics.csv')
print(df1)
print()
df2=pd.read_csv('brics.csv',header=None,index_col=0)
print(df2)
print()


# In[14]:


import pandas as pd
df1=pd.read_csv('brics.csv')
print(df1)
print('--------------------------')
cols=['code','country','population','area','capital']
df2 = pd.read_csv("brics2.csv", header=None, names=cols)
print(df2)
print('--------------------------')
cols2=['country','population','area','capital']
df3 = pd.read_csv("brics2.csv", names=cols2, index_col=0)
print(df3)
print('--------------------------')


# In[15]:


df1=pd.read_csv('area.csv')
print(df1)
print()
df2=pd.read_csv('area.csv',header=0,index_col=0)
print(df2)


# In[16]:


import pandas as pd
df1=pd.read_json('brics.json')
print(df1)
print()
df2=pd.read_json('area.json',encoding='big5')
print(df2)


# In[17]:


get_ipython().system('pip install lxml')


# In[ ]:




