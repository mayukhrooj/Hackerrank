#!/bin/python3

import math
import os
import random
import re
import sys

def find (a):
  for i in range (0, len(a)-1):
    if a[i] == a[i+1]:
      return i+1
  return None

def superReducedString (word):
  if word =="":
    return "Empty String"
  while(True):
    p = find (word)
    if p is None:
      return word
    if p == 1 and len(word) == 2:
      return "Empty String"
    else:
      part1 = word[0:p-1]
      part2 = word[p+1:len(word)]
      word = part1 + part2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
