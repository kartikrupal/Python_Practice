# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:39:16 2024

@author: karti
"""
#%%
def linear_search(data, target):
  
  for i, item in enumerate(data):
    if item == target:
      return i
  return -1

my_list = [1, 3, 5, 7, 9]
target = 7

result = linear_search(my_list, target)

if result != -1:
  print(f"Element found at index: {result}")
else:
  print("Element not found in the list")
#%%
def binary_search_recursive(data, target, low=0, high=None):

  if high is None:
    high = len(data) - 1
  if low == high:  
    return low if data[low] == target else -1
  mid = (low + high) // 2
  if data[mid] == target:
    return mid
  elif data[mid] < target:
    return binary_search_recursive(data, target, mid + 1, high)
  else:
    return binary_search_recursive(data, target, low, mid - 1)
my_list = [1, 3, 5, 7, 9]
target = 7

result = linear_search(my_list, target)

if result != -1:
  print(f"Element found at index: {result}")
else:
  print("Element not found in the list")
  
#%%
def selection_sort(data):
 

  for i in range(len(data)):
    
    min_index = i
    for j in range(i + 1, len(data)):
      if data[j] < data[min_index]:
        min_index = j

    if i != min_index:
      data[i], data[min_index] = data[min_index], data[i]

  return data
my_list = [64, 25, 12, 22, 11]
sorted_list = selection_sort(my_list.copy())  # Avoid modifying the original list

print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")
#%%
def merge_sort(data):
  
  if len(data) <= 1:
    return data

  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])

  return merge(left, right)

def merge(left, right):
  

  merged = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  merged += left[i:]
  merged += right[j:]

  return merged

my_list = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_list = merge_sort(my_list.copy())  

print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")
#%%
def merge_sort(data):


  if len(data) <= 1:
    return data
  mid = len(data) // 2
  left = merge_sort(data[:mid])
  right = merge_sort(data[mid:])

  return merge(left, right)

def merge_q(left, right):
  
  merged = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1

  merged += left[i:]
  merged += right[j:]

  return merged

# Example usage
my_list = [6, 5, 3, 1, 8, 7, 2, 4]
sorted_list = merge_sort(my_list.copy())  # Avoid modifying the original list

print(f"Original list: {my_list}")
print(f"Sorted list: {sorted_list}")


