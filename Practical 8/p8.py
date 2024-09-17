# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 11:30:45 2024

@author: karti
"""

#%%
def hi(str_1):
    str_2="HELLO "+ str_1 +" SIR "
    return str_2;
str_1="KARTIK"
print(hi(str_1))



#%%
def size(length, width):
  
  area = length * width
  perimeter = 2 * (length + width)
  return area, perimeter
length = 5
width = 3
area, perimeter = size(length, width)
print("AREA IS : ",area," PERIMETER IS : ",perimeter)
#%%
def minmax(data):
  a=min(data)
  b=max(data)  
  return a,b
data = [9458,9,59,62,985,62,95,9,59]
min_value, max_value =minmax(data)
print("Minimum value:", min_value," Maximum value: ",max_value)
#%%
def temp(celsius):
 
  fahrenheit = (celsius * 9/5) + 32
  kelvin = celsius + 273.15
  return fahrenheit, kelvin

celsius = 25
fahrenheit, kelvin = temp(celsius)
print(celsius," °C is equal to",fahrenheit," °F and ",kelvin ," K")
#%%
def square(x):
 
  return x * x

def apply(data, func):
 
  return [func(x) for x in data]

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply(numbers, square)
print(squared_numbers)
#%%
import random
import string
def generate_captcha(length):
    captcha = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        captcha += random.choice(characters)
    return captcha

preferred_length = int(input("Enter preferred length for CAPTCHA: "))
captcha = generate_captcha(preferred_length)
print("Generated CAPTCHA:", captcha)
#%%
def multiply(x, y):
    return x * y

def apply_function_with_multiple_args(func, data_x, data_y):
    return [func(x, y) for x, y in zip(data_x, data_y)]
98
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [10, 20, 30, 40, 50]
result = apply_function_with_multiple_args(multiply, numbers1, numbers2)
print(result)
#%%
def get_length(string):
    return len(string)

def sort_strings_by_length(strings):
    return sorted(strings, key=get_length)

words = ["apple", "banana", "cherry", "date", "blueberry"]
sorted_words_by_length = sort_strings_by_length(words)
print(sorted_words_by_length)  # Output: ['date', 'apple', 'banana', 'cherry', 'elderberry']
#%%
def is_even(x):
    return x % 2 == 0

def filter_data(predicate, data):
    return [x for x in data if predicate(x)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter_data(is_even, numbers)
print(even_numbers)

#%%
def square(x):
    return x * x

def apply_function(func, data):
    return [func(x) for x in data]

numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_function(square, numbers)
print(squared_numbers)

#%%
from functools import reduce

def add(x, y):
    return x + y

def aggregate_data(aggregation_func, data):
    return reduce(aggregation_func, data)

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = aggregate_data(add, numbers)
print(sum_of_numbers)  # Output: 15 (1 + 2 + 3 + 4 + 5)

#%%



