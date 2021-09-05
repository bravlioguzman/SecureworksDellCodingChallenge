#!/usr/bin/env python3

#File: Transpose.py

import os
import sys
from functools import reduce
from pathlib import Path

# Making a function to read the file and transpose it
# Loop and read the list of strings in the file
# Iterate between strings to get longest string
# Count the characters, close file and return the transposed string
def longest_word_and_transpose(filename):
   try:
      my_file = open(filename, "r", encoding="utf-8")
      my_string = [y for x in my_file.readlines() for y in x.split()]
      longest = reduce(lambda x, y: y if len(x) < len(y) else x, my_string, "")
      print("Longest word is " + longest +  " and it contains " + str(len(longest)) + " characters")
      str_transposed = str(longest)[::-1]
      print(" ")
      print("The longest word transposed: " + str_transposed)
      my_file.close()
      return str_transposed
   except Exception as e:
      print(e)
      print("Invalid text format, please make sure to pass a valid text file")


def main():
   if len(sys.argv) < 2 or os.path.exists(sys.argv[1]) == 0:
      print("Text File does not exist") 
      exit(0)

   elif os.path.getsize(sys.argv[1]) <= 0:
      print("Looks like the file is empty, please add words to the file")
      exit(0)

   elif Path(sys.argv[1]).suffix != '.txt':
      print("The file must be a text file. Example \"filename.txt\"")
      exit(0)

   else:
      longest_word_and_transpose(sys.argv[1])

if __name__ == "__main__":
    main() 
