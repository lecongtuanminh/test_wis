#!/usr/bin/env python
# coding: utf-8

# In[13]:


a = 0
b = 1
n = int(input('Bạn muốn bao nhiêu số Fibonacci: '))
for i in range(n):
    temp = a + b
    a = b
    b = temp
    print(temp, end =' ')
    

