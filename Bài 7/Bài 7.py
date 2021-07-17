#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def get_digits(num):
    return [int(i) for i in str(num)]
num = random.randint(1000,9999)
print('Hãy đoán con số có 4 chữ số ')
print(num) #nếu muốn biết số
def num_cows_bulls(num,guess):
    cow_bull = [0,0]
    num_list = get_digits(num)
    guess_list = get_digits(guess)
        
    for i,j in zip(num_list,guess_list):
        if j in num_list:
            if j == i:
                cow_bull[0] += 1
            else:
                cow_bull[1] += 1
    return cow_bull
try_count=0
while True:
    guess = int(input("Hãy đoán con số: "))
    try_count+=1
    if guess < 1000 or guess > 9999:
        print("Hãy đoán con số có 4 chữ số")
        continue
        
    cow_bull = num_cows_bulls(num,guess)
    print(f"{cow_bull[0]} cows, {cow_bull[1]} bulls")
    if cow_bull[0] == 4:
        print("Bạn đoán đúng rồi!")
        print('Bạn đã đoán',try_count,'lần')
        break



