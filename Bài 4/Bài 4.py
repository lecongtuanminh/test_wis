#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Error1(Exception):
    pass
    
class Error2(Exception):
    pass
    
while True:
    inp = list(map(str, input("Nhập các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ").split(",")))
    try:
        for item in inp:
            if len(item) != 4:
                raise Error1(print('\nHãy nhập các số có 4 chữ số'))   
        for item in inp:
            for i in range(len(item)):
                if item[i] != '0' and item[i] != '1':
                    raise Error2(print('\nHãy nhập các số nhị phân'))
        
    except (Error1,Error2):
        print('')
    else:
        print ('\nHợp lệ\n')
        break
        
for item in inp: 
    if int(item)%5==0:
        print(item, end=',')

