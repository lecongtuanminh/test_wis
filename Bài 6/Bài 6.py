#!/usr/bin/env python
# coding: utf-8

# In[2]:


num = int(input("Nhập số nguyên dương:"))
factorial = 1
while num>0:
    factorial = factorial * num
    num = num - 1
print('Giai thừa là',factorial)

