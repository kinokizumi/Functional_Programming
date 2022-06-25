#!/usr/bin/python3

########################
#
# This script exploits the difference between iterative recursion and partitionable recursion
#
########################

### Iterations => slow and reach depth limits fast with recursion in python

### Ex.1 ###

def running_sum(numbers):
    if len(numbers) == 0:
        return 0
    total = numbers[0] + running_sum(numbers[1:])
    return total

numbers = list(range(11))
print("Sum = ", running_sum(numbers))

### Ex.2 ###

def factorialR(N):
    assert isinstance(N, int) and N >= 1
    return 1 if N <=1 else N * factorialR(N-1)

def factorialI(N):
    assert isinstance(N, int) and N >= 1
    product = 1
    while N >= 1:
        product *= N
        N -= 1
    return product

print("Recursive factorial = ", factorialR(10))
print("Iterative factorial = ", factorialI(10))

### Fastest way for factorial => functional programming

from functools import reduce
from operator import mul

def factorialHOF(N):
    return reduce(mul, range(1, N+1), 1)    # function, variables, initializer

print("Functional programming factorial = ", factorialHOF(10))

### Partition => less than O(N) time and more intuitive 

### Quicksort a list of numbers

def quicksort(lst):
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [x for x in lst if x == pivot ]
    small = quicksort([x for x in lst if x < pivot])
    large = quicksort([x for x in lst if x > pivot])
    return small + pivots + large

import random

lst = random.sample(range(100), 10)
print("List = ", lst)
print("Sorted list = ", quicksort(lst))
