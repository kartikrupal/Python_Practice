# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:36:33 2024

@author: karti
"""

#%%
str1="PyNaTive"
low=""
upp=""
for char in str1:
    if char.islower():
        low +=char
    else:
        upp +=char
arranged_str=low+upp
print(arranged_str)
#%%
n=len(arranged_str)
for i in range(0,n):
    if (i%2==0):
        print(upp[i])
    elif(i%2!=0):
        print(low[i+2])
        
#%%
set1=[[1,2],[3,4]]
print(set1)
print(type(set1))
#%%
text = "This is a sample string"
# Extract characters from index 7 to 15 (exclusive)
middle_part = text[7:15] # "is a sam"
# Extract everything after the word "is"
after_is = text[3:] # "is a sample string"
# Extract everything before the word "sample"
before_sample = text[:13] # "This is a "

print(middle_part)
print(after_is)