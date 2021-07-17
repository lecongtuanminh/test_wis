#!/usr/bin/env python
# coding: utf-8

# In[39]:


import string
digs = string.digits + string.ascii_letters

def convert():
    num = int(input('Nhập số nguyên :'))
    base = int(input('Nhập cơ số :'))
    ini_num = num

    if num < 0:
        sign = -1
    elif num == 0:
        return digs[0]
    else:
        sign = 1

    num = num*sign
    digits = []

    while num:
        digits.append(digs[int(num % base)])
        num = int(num / base)

    if sign < 0:
        digits.append('-')

    digits.reverse()

    print('số nguyên {} trong hệ cơ số {} là: '.format(ini_num,base), ''.join(digits))


convert()

