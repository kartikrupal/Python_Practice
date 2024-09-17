# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:20:17 2024

@author: karti
"""
'''checking even or odd
leap year 
password checker
bmi calculator
grade 
age group classification 
simple calculator
largest number 
vowel '''

#%%
num1=int(input("enter the value "))
print("the number is ",num1)
num2=int(input("enter the value "))
print("the number is ",num2)
#%%
"""" ARITHMETIC OPERATOR """
sum=num1+num2
print("THE SUM IS : ",sum)

subtraction=num1-num2
print("THE DIFFERENCE IS :  ",subtraction)

multiply=num1*num2
print("THE MULTIPLICATION IS :",multiply)

div=num1/num2
print("THE DIVISION IS :",div)

modulo=num1%num2
print("THE MODULO DIVISION IS:",modulo)

a=25
b=8
c=a//b
print("the floor div: " ,c)

exp=num1**num2
print("EXPONENTIAL :",exp )
#%%
"""" RELATIONAL OPERATOR """
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
#%%
"""" EQUALITY OPERATOR"""
print(num1==num2)
print(num1!=num2)
#%%
"""" LOGICAL OPERATOR"""
a = 10
b = 10
c = -10
if a > 0 and b > 0: 
	print("The numbers are greater than 0") 
if a > 0 and b > 0 and c > 0: 
	print("The numbers are greater than 0") 
else: 
	print("Atleast one number is not greater than 0")
#%%
"""" BITWISE OPERATOR """

print(bin(num1)[2:])
print(bin(num2)[2:])

print("a & b =", a & b)
print("a | b =", a | b)
print("~a =", ~a)
print("a ^ b =", a ^ b)

#%%
'''EXPERIMENT 2'''

a=int(input("enter the value "))
print("the number is ",a)
if(a%2==0):
    print("EVEN NUMBER")
else:
   
   print("ODD NUMBER")
#%%
height = float(input("Enter the height in cm: "))  
weight = float(input("Enter the weight in kg: "))  
 
BMI = weight / (height/100)**2  
print("Your Body Mass Index is", BMI)  
  
if BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif BMI <= 29.9:  
    print("Eee! You are over weight.")  
else:  
    print("Seesh! You are obese.")
    
#%%
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)    
#%%
year = int(input("Enter a year: ")) 
if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
    print("Leap Year")
else:
    print("Not leap Year") 
#%%
age = int(input("ENTER AGE: "))

if age >= 0 and age < 12:
    print("Child")
elif age > 11 and age < 18:
    print("Teen")
elif age > 17 and age < 65:
    print("Adult")
elif age > 64:
    print("Senior")
else:
    print("Invalid age")
