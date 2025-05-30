#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import shutil


# In[2]:


fs_path = "../camino_freesurfer/"


# In[3]:


data_path = "../data/"


# In[4]:


subj_names = os.listdir(fs_path)


# In[6]:


for s in subj_names:
    aparc_aseg_path = fs_path + s + "/mri/aparc+aseg.mgz"
    subj_path = data_path + s + "/aparc+aseg.mgz"
    
    try:
        shutil.copyfile(aparc_aseg_path, subj_path)
    
    except FileExistsError:
        pass

