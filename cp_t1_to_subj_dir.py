#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
import shutil


# In[29]:


t1_parent_path = "../t1_hom_corr/nii/"


# In[14]:


data_path = "../data/"


# In[21]:


t1_names = os.listdir(t1_parent_path)


# In[43]:


old_t1_paths = []
new_t1_paths = []

for n in t1_names:
    old_t1_paths.append(t1_parent_path + n)
    
    current_subj = n.split("_T1")[0]
    new_t1_paths.append(data_path + current_subj + "/t1.nii.gz")


# In[46]:


for op, np in zip(old_t1_paths, new_t1_paths):
    try:
        shutil.copyfile(op, np)
    except FileNotFoundError:
        pass


# In[ ]:




