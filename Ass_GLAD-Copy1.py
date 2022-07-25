#!/usr/bin/env python
# coding: utf-8

# In[469]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[470]:


dat=pd.read_excel('asv.xlsx')


# In[471]:


dat.head(10)


# 

# In[324]:


dat["Scan Month"]=dat["Scan Date"].dt.month
dat["Scan Month"]=dat["Scan Month"].replace({2:"February",3:"March"})
dat


# In[37]:


dat.shape


# In[42]:


dat.nunique()


# In[161]:


dat['Scan Date'].unique


# In[466]:


dat_1=dat[["Has Description?","Video URL","Scan Month"]]


# In[467]:


dat_1


# In[360]:


dat_1.info()


# In[189]:


dat_1_HD=dat_1[dat_1["Has Description?"]=="Has Description"]


# In[190]:


dat_1_HD.count()


# In[191]:


dat_1_DM=dat_1[dat_1["Has Description?"]=="Description Missing"]


# In[192]:


dat_1_DM.count()


# 1. Below dataframe shows videos URL without description

# In[193]:



dat_1_DM


# 2. Videos with comments enabled

# In[495]:



data=dat[["Video URL","Comments?","Scan Month"]]
data_1=data[data["Comments?"]=="Comments Enabled"]
data_1


# 3. video with less than 100 views

# In[493]:


view=dat[["Video URL","Views","Scan Month"]]
view=view[view['Views']<100]
view


# 4. Channels without location

# In[299]:


loc=dat[["Brand","Title","Video URL","Location?","Scan Month"]]
loc_1=loc[loc["Location?"]=="No Location"]
loc_1


# 5. Number of views for Brand

# In[446]:



br=dat.sort_values(['Views'],ascending=False).groupby('Brand')
br
type(br)
# for i,j in br:
#     display(br.get_group(i))


# 6. Video URL which has Monitoring Id
#    *only 15 rows has Monitoring id

# In[327]:


Mon=dat[["Video URL","Monitoring ID"]]
ID=Mon[Mon["Monitoring ID"]=="IDM 02688"]
ID.head(100)


# 7. Total number of views for Video URL 

# In[325]:


URL=dat[["Video URL","Views"]]
URL.groupby(["Video URL"]).sum()
display(URL)


# 8. Total Views for Brand 

# In[461]:




bm=dat.groupby(['Brand']).sum()
bm=bm.sort_values(by='Views',ascending=False)
bm


# In[465]:


Ma=dat.groupby(["Market"]).sum()
Ma=Ma.sort_values(by='Views',ascending=False)
Ma.head(5)


# 
