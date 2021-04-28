#!/usr/bin/env python
i = int(input("Enter number"))
for num in xrange (1, i+1):
    if num % 5 == 0:
        print (num)



def fizbuzz(number):
    div5 = False
    if num % 5 == 0:
        div5 = True
    div15 = False
    if num % 15 == 0:
        div15 = True
    if div5 and div15:
        return "fizbizzbizz"
    elif div5 and not div15:
        return "bizz"
    elif div15 and not div5:
        return "fizzbizz"
    else:
        return None

range = in