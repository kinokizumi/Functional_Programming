#!/usr/bin/python3

#############
#
# This script explores different methods of classes
#
#############

## Accessors: take no arguments as getters and return no value as setters

class Car(object):
    def __init__(self):
        self.vel = 100

    @property
    def speed(self):
        print("Speed is", self.vel)
        return self.vel

    @speed.setter
    def speed(self, value):
        print("Setting speed to", value)
        self.vel = value

car = Car()
car.speed = 80
car.speed

## Operators: co-opt the syntax of assignment to pass an argument

class TalkativeInt(int):
    def __lshift__(self, other):
        print("Shift", self, "by", other)
        return int.__lshift__(self, other)

t = TalkativeInt(8)
print(t << 3)

## Static Methods of Instances: use as namespaces for related functions

import math
class RightTriangle(object):
    @staticmethod
    def hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)

    @staticmethod
    def sin(a, b):
        return a / RightTriangle.hypotenuse(a, b)

    @staticmethod
    def cos(a, b):
        return b / RightTriangle.hypotenuse(a, b)

rt = RightTriangle()
print(rt.hypotenuse(3, 4))
print(rt.sin(3, 4))
print(rt. cos(3, 4))

## without decorators -> cannot work on the instance (need to pass self)

import functools, operator
class Math(object):
    def product(*nums):
        return functools.reduce(operator.mul, nums)
    def power_chain(*nums):
        return functools.reduce(operator.pow, nums)

print(Math.product(3,4,5))
print(Math.power_chain(2,3,4))

m = Math()
# print(m.product(3,4,5))      # error since self is not passed in operators

## Generator Functions: yield an interator that produces a sequence when called with next() or looped over

def get_primes():
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

primes = get_primes()
print(next(primes), next(primes), next(primes))
for _, prime in zip(range(10), primes):
    print(prime, end=" ")       # to rewind generator, rerun the function
print("")


