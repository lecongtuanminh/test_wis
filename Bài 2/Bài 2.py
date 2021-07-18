#!/usr/bin/env python
# coding: utf-8

# In[22]:


a = 1
b = 1
n = int(input('Bạn muốn bao nhiêu số Fibonacci: '))
for i in range(n):
    temp = a
    a = b
    b = temp + b
    print(temp, end =' ')
    

