#!/usr/bin/env python

"""
# input a number
# if number is divisible by 3 then print foo
# if number is divisible by 5 then print bar
# if number is divisible by both 3 and 5 then print foobar
"""

# number = int(input("Input a number: "))
# if number % 3 == 0:
#     print("foo", end='')
# if number % 5 == 0:
#     print("bar", end='')
# print()


"""
if the number is not divisible by any then dont print an extra line
"""

# number = int(input("Input a number: "))
# if number != 0:
#     divisibility3 = False
#     divisibility5 = False
#     if number % 3 == 0:
#         print("foo", end='')
#         divisibility3 = True
#     if number % 5 == 0:
#         print("bar", end='')
#         divisibility5 = True
#     if divisibility3 or divisibility5:
#         print()

"""
do this for all integers which are multiples of 6 till 500
"""
 
# for number in range(6,500,6):
#     print(f"{number} :", end='')
#     divisibility3 = False
#     divisibility5 = False
#     if number % 3 == 0:
#         print("foo", end='')
#         divisibility3 = True
#     if number % 5 == 0:
#         print("bar", end='')
#         divisibility5 = True
#     if divisibility3 or divisibility5:
#         print()

"""
Dont show numbers which are divisible by anything
"""

# for number in range(2,500,2):
#     divisibility3 = False
#     divisibility5 = False
#     if number % 3 == 0:
#         divisibility3 = True
#     if number % 5 == 0:
#         divisibility5 = True
#     if divisibility3 or divisibility5:
#         print(f'{number}: {"foo" if divisibility3 else ""}{"bar" if divisibility5 else ""}') 


"""
foo: "Number", bar: "number"
"""

# foobar = []
# foo = []
# bar = []
# for number in range(2,500,2):
#     divisibility3 = False
#     divisibility5 = False
#     if number % 3 == 0:
#         divisibility3 = True
#     if number % 5 == 0:
#         divisibility5 = True
#     if divisibility3 or divisibility5:
#         if divisibility3 and divisibility5:
#             foobar.append(number)
#         if divisibility3 and not divisibility5:
#             foo.append(number)
#         if divisibility5 and not divisibility3:
#             bar.append(number)
# print(f'foobar: {foobar}')
# print(f'foo: {foo}')
# print(f'bar: {bar}')

# x = int(len(foo) * 0.8)
# y = int(len(bar) * 0.8)
# z = int(len(foobar) * 0.8)
# print(f'foo 80th percentile value is at {x-1}/{len(foo)}: {foo[x-1]}')
# print(f'bar 80th percentile value is at {y-1}/{len(bar)}: {bar[y-1]}')
# print(f'foobar 80th percentile value is at {z-1}/{len(foobar)}: {foobar[z-1]}')

"""
for each number N in foobar. P = # numbers in foo are lesser than N, Q = # number in bar are more than N
N P Q
30 4 31
"""
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 
foobar = []
foo = []
bar = []
for number in range(2,500,2):
    divisibility3 = False
    divisibility5 = False
    if number % 3 == 0:
        divisibility3 = True
    if number % 5 == 0:
        divisibility5 = True
    if divisibility3 or divisibility5:
        if divisibility3 and divisibility5:
            foobar.append(number)
        if divisibility3 and not divisibility5:
            foo.append(number)
        if divisibility5 and not divisibility3:
            bar.append(number)
print(f'foobar: {foobar}')
print(f'foo: {foo}')
print(f'bar: {bar}')

# for n in foobar :

