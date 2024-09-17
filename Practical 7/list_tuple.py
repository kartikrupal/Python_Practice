# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:44:51 2024

@author: karti
"""
#%% find the second largest number
def seclarg(tuple_1):
    b=list(tuple_1)
    b.sort()
    tuple_1=tuple(b)
    return tuple_1[-2]
tup=(2,6,59,5,89,102,63,5,6)
print("THE SECOND LARGEST NO.:",seclarg(tup))
#%% find cumulative sum of tuple
n=len(tup)
sum=0
for i in range(0,n):
    sum=sum+tup[i]
print("the cumulative sum is ", sum)

#%% mode of tuple
maxcount=0
mode=0
for i in tup :
      count = tup.count(i)
      if maxcount <  count:
            maxcount = count
            mode = i
print("mode:", mode)
#%% divide tupple into chunks
tuple_2=(1,2,3,4,5)
def divide_chunks(l, n): 
      for i in range(0, len(l), n):  
        print( l[i:i + n] ) 
n = 2
divide_chunks(tuple_2, n) 
#%% find common element from 3 tupple
t1 = (1, 2, 3, 4)
t2 = (3, 4, 5, 6)
t3 = (4, 5, 6, 7)
t4= []
for item in t1:
    if item in t2:
        if item in t3:
            t4.append(item)
print("Element present in all tuple is ", t4)
#%%


#%%
#%% second largest
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
my_list.sort(reverse=True)
print("SECOND LARGEST NUMBER IS:",my_list[1])
#%% cumulative sum 

n=len(my_list)
sum=0
for i in range(0,n):
    sum=sum+my_list[i]
print("the cumulative sum is ", sum)

#%% mode 

maxcount=0
mode=0
for i in my_list :
      count = my_list.count(i)
      if maxcount <  count:
            maxcount = count
            mode = i
print("mode:", mode)

#%%
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

chunks = []
for i in range(0, len(my_list), chunk_size):
    chunks.append(my_list[i:i + chunk_size])

print(chunks)

#%%
list1=[4,5,6,8]
list2=[8,5,2,3,1]
list3=[7,8,9,6,5,41,3,3]
t4= []
for item in list1:
    if item in list2:
        if item in list3:
            t4.append(item)
print("Element present in all list is ", t4)

#%%
a={1}
print(type(a))
a=set()
print(type(a))


