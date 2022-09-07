#!/usr/bin/python3

#################
#
# This script shows the difference between a class and a closure
#
#################

## Classes emphasize mutable/rebindable state

class Adder(object):
    def __init__(self, n):
        self.n = n
    def __call__(self, m):
        return self.n + m

add5_i = Adder(5)
print(add5_i(10))

add5_i.n = 10           # state is readily changeable
print(add5_i(10))

## Closures emphasize immutability and pure functions

def make_adder(n):
    def adder(m):
        return m + n
    return adder

add5_f = make_adder(5)
print(add5_f(10))

## Manufature several related closures

## impure

adders = []
for n in range(5):
    adders.append(lambda m: m+n)    # n is mutable thus the last value overrides all previous 

print([adder(10) for adder in adders])

n = 10           # function is modified
print([adder(10) for adder in adders])

## pure

adders = []
for n in range(5):
    adders.append(lambda m, n=n: m+n)

print([adder(10) for adder in adders])

n = 10      # not affecting the function
print([adder(10) for adder in adders])

add4 = adders[4]
print(add4(10, 100))    # override the bound value n
