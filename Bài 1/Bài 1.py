#!/usr/bin/env python
# coding: utf-8

# In[10]:


chuoi_nhap  =str(input('Hãy nhập chuỗi:'))
chuoi_dao = chuoi_nhap[::-1]
if chuoi_nhap == chuoi_dao:
    print('Chuỗi là palindrome')
else:
    print('Chuỗi không phải là palindrome')



