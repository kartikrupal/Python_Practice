# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:21:05 2024

@author: karti
"""
#%% 
# 4 example of for loop and 4 of while 3 given and 1 by choice
'''countdown crete
sum of natural numbers
password validation while loop until correct and after 3 break
factorial calculate
guess the number game while loop
reverse a number like 4569 to 9654
multiplication table of any number
count vowel
right angle triangle with *
sum of square of list of numbers 
string reverse

'''
#%% 
# factorial of a number
a=int(input("Enter a number : "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print("factorial:",fact)
#%%
# multiplication table
num=int(input("Enter a number : "))
for i in range(0,11):
    mul=num*i
    print(num,"X",i,'=',mul)
    
#%%
# sum of natural numbers
sum=0
n=15
for i in range(0,n):
    sum=sum+i
    i=i+1
    
print("THE SUM IS : ",sum)
#%%
#prime num b/w 0 to 20
for num in range(0,20):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num) 
#%%
#password checker
password="Kartik" 
count=0
while count<3:
    pas=input("ENTER THE PASSWORD:")
    count=count+1
    if password==pas:
        print("password is correct")
        break
    else:
        print("password is incorrect")
#%%
#countdown crete
num=int(input("ENTER A NUMBER:"))
while(num>=0):
    if num==0:
        print("COUNTDOWN END")
        break
    else:
        print(num)
        num=num-1  
    
#%%
#Vowel count
a=input("enter anything: ")
count=0
index=0
vowel="aeiouAEIOU"
while index < len(a):
    if a[index] in vowel:
        count=count+1
    index=index+1


print("VOWEL COUNT:",count)
#%%
#print even numbers  b/w given range 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

if num1 > num2:
    while num2 <= num1:
        if num2 % 2 == 0:
            print(num2)
        num2 += 1
else:
    while num1 <= num2:
        if num1 % 2 == 0:
            print(num1)
        num1 += 1
                   
#%%
i=0
while(i<4):
    print("THE i value is", i)
    i=i+1
else:
    print("else block")
#%%
for letter in "KARTIK":
    if letter=="T":
        continue
    print("aplhabet ", letter)
#%%
i = 45
while i > 35:
  i -= 1
  if i == 38:
    break
  print(i)

#%%
i=30
while i%2==0:
    i=i+2
    if i==50:
        break
    print(i)
#%%
i=0
while i>-5:
    i-=1
    print(i)

#%%
kr = ["kartik", "rupal", "kr"]
for x in kr:
    print(x)
#%%
k="kartik"
for a in k:
    if a=="i":
        break
    print(a)


