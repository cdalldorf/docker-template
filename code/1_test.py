#!/usr/bin/env python
# coding: utf-8

# In[1]:


# this is a test notebook


# In[2]:


import socket


# In[4]:


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)


# In[6]:


f = open('../output/delete_me', 'wb')
f.close()


# In[ ]:





# In[ ]:




