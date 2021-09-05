#!/usr/bin/env python3

#File: Transpose.py

import os
from functools import reduce

# Just reading and printing the original file for testing purposes
if os.path.exists("Words.txt") == 0:
    print("File \"Words.txt\" does not exist")
    exit()
elif os.path.getsize("Words.txt") <= 0:
    print("Looks like file is empty. Please add words to the file")
    exit()
else:    
    my_file = open("Words.txt", "r", encoding="utf-8")
    print("##########################")
    print("Reading the original file:")
    print("##########################")
    print(" ")
    print(my_file.read())
    print("##########################")
    print("End of original file")
    print("##########################")
    my_file.close()

# Making a function to read the file and transpose it
# Loop and read the list of strings in the file
# Iterate between strings to get longest string
# Count the characters, close file and return the transposed string
def longest_word_and_transpose(filename):
   my_file = open(filename, "r", encoding="utf-8")
   my_string = [y for x in my_file.readlines() for y in x.split()]
   longest = reduce(lambda x, y: y if len(x) < len(y) else x, my_string, "")
   print("Longest word is " + longest +  " and it contains " + str(len(longest)) + " characters")
   str_transposed = str(longest)[::-1]
   print(" ")
   print("The longest word transposed: " + str_transposed)
   my_file.close()
   return str_transposed

def main():
    longest_word_and_transpose("Words.txt")

if __name__ == "__main__":
    main() 
