#%%
str1="ananya"
print(str1[-3]," ",str1[2])
print(str1[0:5])
#%%
n=len(str1)
for i in range(0,n):
   print(str1[i],end='\t')
print("\n")
m=len(str1)
for i in reversed(range(0,m)):
   print(str1[i],end='\t')
str2='Sharma'
str3=list(str1+str2)
print("\n",str3)
print(str3[0:6:1])
print(str2[6::-1])
str4="kartik  kr rupal"
print(str4[:len(str4)//2])
#%%
str5="I am Muglesh Babu"
for i in tuple(str5):
   print(i,end="")

