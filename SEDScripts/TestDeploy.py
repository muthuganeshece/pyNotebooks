#!/usr/bin/env python
# coding: utf-8

# In[33]:


import os
import sys


# In[34]:

print(len(sys.argv), sys.argv[0], sys.argv[1], os.path.isdir(sys.argv[2]))
path = sys.argv[1]

if os.path.isdir(path) == False:
    path = sys.argv[2]
directories = os.listdir(path)
directories = [path + '\\' + dirs for dirs in directories]

for i in range (len(directories)):
    print(directories[i])


# In[ ]:




