#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df1 = pd.read_html("brics.html")
print(df1)
print('--------------------------')
df2 = pd.read_html('area.html', encoding='utf-8')
print(df2)
print('--------------------------')


# In[2]:


import pandas as pd
df1=pd.read_csv('brics.csv',header=0,index_col=0)
print(df1['country'])
print('---------------------')
print(df1.capital)


# In[3]:


import pandas as pd
df1=pd.read_csv('brics.csv',header=0,index_col=0)
print(df1.loc['BR'])
print()
print(df1.loc['CH'])


# In[4]:


import pandas as pd
df1 = pd.read_csv("brics.csv", header=0, index_col=0)
print(df1['capital'].loc['CH'])
print('-----------------------------')
print(df1.loc['CH']['capital'])
print('-----------------------------')
print(df1.loc['CH', 'capital'])


# In[5]:


import pandas as pd
df=pd.read_csv('area.csv', header=0, index_col=0)
print(df)
print()
print(df[2:5])
print()
print(df[1:10:2])
print()
print(df[4:])
print()
print(df[:5])
print()
print(df['fifth':'ninth'])


# In[6]:


import pandas as pd
df= pd.read_csv('area.csv', header=0, index_col=0)
print(df)
print("---------------------")
print(df["city"])
print("---------------------")
print(df[["population","name"]])
print("---------------------")
print(df[2:5][["city","name"]])
print("---------------------")
print(df[:][['population','city']])
print("---------------------")
print(df['fifth':'ninth']["name"])
print("---------------------")


# In[7]:


import pandas as pd
df = pd.read_csv('area.csv', header=0, index_col=0)
print(df)
print("---------------------")
print(df.iloc[2, 2])
print("---------------------")
print(df.iloc[[5,7,9], 0])
print("---------------------")
print(df.iloc[4, [1, 2]])
print("---------------------")
print(df.iloc[4:9, 2])
print("---------------------")
print(df.iloc[10,:])
print("---------------------")
print(df.iloc[:,[1,0]])
print("---------------------")
print(df.iloc[4:9, 0:3])
print("---------------------")
#print(df.iloc[4:9, "name"])
#print(df.iloc["first", 0:2])


# In[8]:


import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo)
print()
print(ufo.head(10))
print()
print(ufo[['City','State','Time']].tail())
print()
print(ufo.loc[:,['City','State','Time']].sample(6))
print()
print(ufo.loc[10:500:10,['City','State','Time']].sample(frac=0.1))


# In[9]:


import pandas as pd
df=pd.read_csv('area.csv',header=0,index_col=0)
print(df.nlargest(3,'population'))
print(df.nsmallest(4,'population'))


# In[10]:


import pandas as pd
df1=pd.read_csv('brics.csv',header=0,index_col=0)
max_area=df1['area'].max()
print(df1[df1['area']==max_area])
print()
import numpy as np
df2=pd.read_csv('area.csv', header=0, index_col=0)
min_pop=np.min(df2['population'])
print(df2[df2['population']==min_pop])


# In[11]:


import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo['City'].head(10))
print()
ufo['location']=ufo.City+','+ufo.State
print(ufo['location'].head(10))


# In[12]:


import pandas as pd
df=pd.read_csv('area.csv', header=0, index_col=0)
print(df)
print()
city=print(df.pop('city'))
print()
print(df)
print(city)
print()
del df['population']
print(df)


# In[13]:


import pandas as pd
df=pd.read_csv('area.csv', header=0, index_col=0)
print(df)
print()
home=pd.DataFrame({"name":"士林區","population":287214,"city":"台北市"}, index=["fourteen"])
df1=df.append(home)
print(df1)
print()
df2=pd.concat([df,home])
print(df2)


# In[14]:


import pandas as pd
home = pd.DataFrame({"name":"士林區","population":287214,"city":"台北市"}, index=["fourteen"])
df=pd.read_csv('area.csv',header=0,index_col=0).append(home)
print(df)
print("---------------------")
df3 = df.drop('fourteen',axis=0)
print(df3)
print("---------------------")
df4 = df.drop(index='fourteen')
print(df4)
print("---------------------")


# In[15]:


import pandas as pd
df1 = pd.read_csv("brics.csv", header=0, index_col=0)
print(df1)
print('--------------------------')
print("ndim", df1.ndim)
print("shape", df1.shape)
print("size", df1.size)
print("index", df1.index)
print("columns", df1.columns)
print('--------------------------')
print("info():")
print(df1.info())
print("count():")
print(df1.count())
print("describe():")
print(df1.describe())
print('--------------------------')
print("sum():")
print(df1.sum())
print("population mean():", df1['population'].mean())
print("area median():", df1.area.median())
print("population min():", df1['population'].min())
print("population max():", df1['population'].max())
print("std():")
print(df1.std())


# In[16]:


import pandas as pd
import numpy as np
df=pd.DataFrame(np.random.randn(5,3),index=['a', 'c', 'e', 'f','h'],columns=['one', 'two', 'three'])
df=df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)


# In[17]:


import pandas as pd
import numpy as np
df= pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'], columns=['one', 'two', 'three'])
df= df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df['one'].isnull( ) )
print(df.isnull( ) )


# In[18]:


import pandas as pd
import numpy as np
df= pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f','h'], columns=['one', 'two', 'three'])
df= df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df['one'].notnull( ) )
print(df.notnull( ) )


# In[19]:


import pandas as pd
import numpy as np
raw_data= {'first_name': ['Jason', np.nan, 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', np.nan, 'Ali', 'Milner', 'Cooze'],
'age': [42, np.nan, 36, 24, 73],
'sex': ['m', np.nan, 'f', 'm', 'f'],
'preTestScore': [4, np.nan, np.nan, 2, 3],
'postTestScore': [25, np.nan, np.nan, 62, 70],
'testdata': [14, np.nan, 2, 22, 33]}
df= pd.DataFrame(raw_data, columns=['first_name', 'last_name', 'age', 'sex', 'preTestScore',
'postTestScore','testdata'] )
print(df)


# In[20]:


data=df
print(data)
print()
df_drop_any=data.dropna()
print(df_drop_any)
print()
df_drop_all=data.dropna(how='all')
print(df_drop_all)


# In[21]:


import numpy as np
data=df
data['location']=np.nan
print(data)
print("----------------------------------------")
df_drop_col= data.dropna(axis=1, how='all')
print(df_drop_col)
print("----------------------------------------")
df_drop_thresh= data.dropna(thresh=6)
print(df_drop_thresh)
print("----------------------------------------")
df_drop_thresh= data.dropna(thresh=5)
print(df_drop_thresh)
print("----------------------------------------")


# In[22]:


import pandas as pd 
import numpy as np
raw_data={'first_name': ['Jason', 'Jason', 'Jason','Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Miller', 'Miller','Ali', 'Python', 'Pcschool'],
'age': [42, 42, 42, 36, 24, 73],
'preTestScore': [4, 4, 4, 31, 2, 3],
'postTestScore': [25, 25, 25, 57, 62, 70],
'testdata':[3,3,3,3,3,3]}
df=pd.DataFrame(raw_data,columns=['first_name', 'last_name', 'age', 'preTestScore','postTestScore','testdata'])
print(df)


# In[23]:


data=df
print(data)
print("---------------")
print(data.duplicated())
print("---------------")
print(data.duplicated('age'))
print("---------------")
print(data.duplicated('testdata'))


# In[24]:


data = df
print(data)
print("---------------")
print(data.duplicated(subset=['preTestScore','postTestScore'],keep=False))
print("---------------")
print(data.duplicated(subset=['preTestScore','postTestScore']))
print("---------------")


# In[25]:


import pandas as pd
user_cols= ['user_id', 'age', 'gender', 'occupation', 'zip_code']
url= 'http://bit.ly/movieusers'
users = pd.read_table(url, sep='|', header=None, names=user_cols, index_col='user_id')
print(users)
print(users.zip_code.duplicated())
print("---------------")
dup_count=users.zip_code.duplicated().sum()
print(dup_count)
print("---------------")
zips=users.zip_code.unique()
print(len(zips))
print("---------------")


# In[26]:


data = df
print(data)
print("---------------")
print(data.drop_duplicates( ))
print("---------------")
print(data.drop_duplicates(keep='last'))
print("---------------")
print(data.drop_duplicates(keep=False))


# In[ ]:




