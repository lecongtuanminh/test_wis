#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
num = int(input("Nhập số: "))


if num > 1:
   for i in range(2,math.floor(math.sqrt(num))):
       if (num % i) == 0:
           print(num,"không phải là số nguyên tố")
           break
   else:
       print(num,"là số nguyên tố")
else:
   print(num,"không phải là số nguyên tố")

