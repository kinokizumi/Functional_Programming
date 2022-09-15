#!/usr/bin/python3

###############
#
# This script helps to understand the basics of decorators
#
###############

## Simple Decorators: wrap a function, modifying its behavior

def my_deco(func):
    def wrapper():
        print("Before calling function.")
        func()
        print("After calling function.")
    return wrapper

def say_hi():
    print("Hello!")

say_hi = my_deco(say_hi)
say_hi()
print(say_hi)

## The Pie Syntax: @symbol

def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper

@do_twice
def say_whee():
    print("Whee!")

say_whee()

## Decorating Funcitons with Arguments

def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@do_twice
def greet(name):
    print(f"Hello {name}!")

greet("Charlie")

## Return Values from Decorated Functions

import functools

def my_deco(func):
    @functools.wraps(func)           # conserves function ID
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_deco
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}!"

hi_adam = return_greeting("Adam")
print(hi_adam)
print(return_greeting)
print(return_greeting.__name__)

## Real World Example: Print Runtime of Function

import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        runtime = end - start
        print(f"Finished {func.__name__!r} in {runtime:.4f} secs")
    return wrapper

@timer
def sum_square(num_repeat):
    for _ in range(num_repeat):
        sum([i**2 for i in range(10000)])

sum_square(1)
sum_square(100)

## lru_cache: reduces execution time by using memoization technique

from functools import lru_cache
import time

def fib_without_cache(n):
    if n < 2:
        return n
    return fib_without_cache(n-1) + fib_without_cache(n-2)

begin = time.time()
fib_without_cache(30)
end = time.time()
print("Time taken without cache is", end-begin)

@lru_cache(maxsize=128)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)

begin = time.time()
fib_with_cache(30)
end = time.time()
print("Time taken with cache is", end-begin)

## total_ordering: provide class comparison methods (lt, le, eq, ne, gt, ge)

from functools import total_ordering

@total_ordering
class employee:
    def __init__(self, height):
        self.height = height

    def __lt__(self, other):
        return self.height < other.height

print( employee(175) > employee(165) )
print( employee(175) < employee(165) )

