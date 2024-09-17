# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 11:19:44 2024

@author: karti
"""

#%%
def filter_sentences(input_file, output_file):
 
  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
      line = line.strip()
      if 'not' not in line.lower():  
        f_out.write(line + '\n')

input_file = 'input.txt'
output_file = 'output.txt'
filter_sentences(input_file, output_file)

print(f"Sentences without 'not' written to: {output_file}")
#%%
def remove_negative_lines(input_file, output_file, negative_words):

  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    for line in f_in:
      # Check for complete matches of negative words (not substrings)
      if not any(word in line.lower() for word in negative_words):
        f_out.write(line)

input_file = "D:\AIML SEM 4\python\practical 10.1\input.txt"
output_file = "output.txt"
negative_words = ["sad", "angry", "hate", "terrible"]

remove_negative_lines(input_file, output_file, negative_words)
print(f"Lines containing negative words removed and saved to: {output_file}")
