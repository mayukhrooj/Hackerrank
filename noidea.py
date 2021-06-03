#!/usr/bin/env python
N = input().split()
M = input().split()
A = set(input().split)
B = set(input().split)

Happiness = 0
for i in N:
    if i in A:
        Happiness += 1
    if i in B:
        Happiness -= 1
print(Happiness)
