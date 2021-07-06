#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Question 1
x = np.arange(0,10)
y = x*x
plt.title("squares")
plt.plot(x,y, color='r')
plt.show()


# In[3]:


# Question 2
a = [1,2,3,4,5,6,7] # days
b = [160, 150, 140, 145, 175, 165, 180] # sales

plt.figure(figsize = (8,4))
plt.title("Sales Graph")
plt.xlabel("days")
plt.ylabel("sales")
plt.plot(a,b, 'go', linewidth = 2,markersize = 8)


# In[ ]:




