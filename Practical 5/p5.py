# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 11:23:32 2024

@author: karti
"""

#%%
list=['kartik',15,'kr',840,448]
print(list[3])
print(list[-1])
print(len(list))
list.append("chandigarh")
print(list)

list.insert(3,827)
print(list)

print(list.count(448))
print(list)

list_2=['kr04','pb08']
list.extend(list_2)
print(list)

list.remove(448)
print(list)

list.pop()
print(list)

list.reverse()
print(list)

list_3=[5,654,494,6494,9949,495,49,64,9654,9]
list_3.sort()
print(list_3)

list4=list_3.copy()
print("LIST COPY:",list4)

#%%
S="i am happy" 
str=''
arr=[]
for i in S:
    if S==" ": 
        str=S
        break
    else:
        arr.append(S)
print(arr)
        
    
#%%
string= "I am Happy"
words = []
str= ""
for i in string:
    if i.isspace():
        if str:
            words.append(str)
            str = ""
    else:
        str += i

if str:
    words.append(str)

print(words)
#%%
#%%
# Create an initial list
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Display the length of the list
print("Length of the list:", len(my_list))

#index for list
k=my_list.index(5)
print(f"your index is : {k}")
my_list.append(448)
#count in list
a=my_list.count(5)
print(f"your count is {a}")

# Insert an element at a specific index
my_list.insert(2, 7)
print("After insertion:", my_list)

# Extend the list with another list
my_list.extend([8, 9, 10])
print("After extension:", my_list)

# Remove the first occurrence of a value
my_list.remove(5)
print("After removal:", my_list)

# Pop an element from a specific index
popped_element = my_list.pop(4)
print("Popped element:", popped_element)
print("After popping:", my_list)

# Reverse the list
my_list.reverse()
print("After reversing:", my_list)

# Sort the list
my_list.sort()
print("After sorting:", my_list)

# Make a copy of the list
copied_list = my_list.copy()
print("Copied list:", copied_list)




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














