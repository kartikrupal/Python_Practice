#%%
t=()
t_1=(1)
t_2=(1,)
print(type(t))
print(type(t_1))
print(type(t_2))
#%%
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#%%
tup=(1,2,3,4,5)
print("First element:", tup[0])
print("Last element:", tup[-1])
print("Slice from index 1 to 3:", tup[1:4])
print("Length of tuple:", len(tup))
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2
print("Concatenated tuple:",tup3)
tup4 = tup3 * 2
print("Repeated tuple:",tup4)
print("Is 3 present in the tuple?", 3 in tup4)
print("Iterating through the tuple:")
for item in tup1:
    print(item)


a, b, c, d, e = tup
print("Unpacked variables:", a, b, c, d, e)


print("Minimum element:", min(tup))
print("Maximum element:", max(tup))


my_list = [6, 7, 8, 9, 10]
converted_tuple = tuple(my_list)
print("Converted tuple from list:", converted_tuple)
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
tup_1=(2,6,59,5,89,102,63,5,6)
tup_2=sorted(tup_1)
print(tup_2[-2])




