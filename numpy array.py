#!/usr/bin/env python
# coding: utf-8

# In[85]:


import numpy as np
arr1 = np.array([1,2,3])
print(arr1)


# In[23]:


arr1[2]


# In[3]:


arr1[2]=5


# In[4]:


arr1


# In[11]:


arr2 =np.array([[1,2,3],[4,5,6]])
print(arr2)


# In[12]:


print("the shape is 2 row and 3 columns:",arr2.shape)


# In[10]:


print(arr2[0][2])
print(arr2[0,2])
print(arr2[0,-1])
print(arr2[-1,0])


# In[14]:


arr3=np.array(['India','china','usa','mexico'])
print(arr3)


# In[16]:


arr3[3]


# In[27]:


arr=np.arange(0,20,2)
print(arr)


# In[40]:


arr=np.linspace(0,2,20)
print(arr)


# In[41]:


arr=np.random.rand(10)
print(arr)
print('\n')
arr= np.random.rand(3,4)
print(arr)


# In[46]:


print(np.full((5,4),1.1))


# In[49]:


arr=[0,1,2]
print(np.repeat(arr,4))


# In[52]:


arr=[0,1,2]
print(np.tile(arr,3))


# In[53]:


identity_matrix=np.eye(3)
print(identity_matrix)


# In[54]:


identity_matrix=np.identity(3)
print(identity_matrix)


# In[56]:


arr=np.random.rand(5,5)
print(arr)


# In[59]:


print(np.sum(arr,axis=0))


# In[62]:


print(np.sum(arr,axis=1))


# In[63]:


print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))


# In[66]:


arr=np.random.rand(5,5)
print(arr)


# In[67]:


print(np.sort(arr,axis=1))


# In[68]:


arr=np.array([4,5,6,7])


# In[73]:


arr1=np.append(arr,8)
arr1


# In[75]:


arr2=np.append(arr,[9,10,11])
print(arr2)


# In[78]:


arr2=np.array([4,5,6,7,8,9,10,11])
print(arr2)
print('\n')
arr5=np.delete(arr2,[1,4])
print(arr5)


# In[79]:


arr1=np.array([[1,2,3,4,],[1,2,3,4]])
arr2=np.array([[5,6,7,8],[5,6,7,8]])


# In[80]:


cat=np.concatenate((arr1,arr2),axis=0)
print(cat)


# In[83]:


cat=np.concatenate((arr1,arr2),axis=1)
print(cat)


# In[ ]:




