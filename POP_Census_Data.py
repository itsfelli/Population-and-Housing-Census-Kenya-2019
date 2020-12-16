#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# # Loading Data 
# 

# ## 1st dataset: Kenya population density per county per Land area

# In[76]:


df = pd.read_csv("https://open.africa/dataset/9b94fe50-9d75-4b92-be00-6354c6e6cc88/resource/da01bf5a-61d7-43e5-9009-7b54e249e984/download/kenya-population-land-area-population-density_by_county.csv")


# In[77]:


df.head(15)



# ## Formatting the first data set

# In[78]:


#Labelling the columns
df.columns=('County_Name','Pop_Size','Land_Area(Sq.Km)','Pop_density_per_Sqkm')


# In[79]:


df.head(15)


# In[82]:


#deleting the first few rows that have unwanted information
df.drop(df.index[:7], inplace=True)


# In[83]:


df.head()


# In[84]:


df


# In[85]:


#resetting the index
df.reset_index(drop= True, inplace=True)


# In[87]:


df


# ## Loading the second dataset:

# In[ ]:




