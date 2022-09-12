#!/usr/bin/python3

################
#
# This script explores the iterator protocol in python
#
################

## To achieve lazy data structure

from collections.abc import Sequence

class ExpandingSequence(Sequence):
    def __init__(self, it):
        self.it = it
        self._cache = []
    def __getitem__(self, index):
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]
    def __len__(self):
        return len(self._cache)

def get_primes():
    candidate = 2
    found = []
    while True:
        if all(candidate % prime != 0 for prime in found):
            yield candidate
            found.append(candidate)
        candidate += 1

primes = ExpandingSequence(get_primes())
print(len(primes))
for _, p in zip(range(10), primes):
    print(p, end=" ")
print("")
print(primes[5])
print(primes[20])
print(len(primes))

## An iterator has a method name .__iter__() and .__next__()

lazy = open('README.md')
print('__iter__' in dir(lazy) and '__next__' in dir(lazy))

plus5 = map(lambda x: x+5, range(10))
print('__iter__' in dir(plus5) and '__next__' in dir(plus5))
print(list(plus5))

def to10():
    for i in range(10):
        yield i

print(to10, to10(), next(to10()))
print('__iter__' in dir(to10()) and '__next__' in dir(to10()))

l = [1, 2, 3]
print('__iter__' in dir(l), '__next__' in dir(l))

li = iter(l)
print(li)
print(li == iter(li))

## Classes with iterator protocol

from collections.abc import Iterable

class Fibonacci(Iterable):
    def __init__(self):
        self.a, self.b = 0, 1
        self.total = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        self.total += self.a
        return self.a
    def running_sum(self):
        return self.total

fib = Fibonacci()
print(fib.running_sum())
for _, i in zip(range(10), fib):
    print(i, end=" ")
print("")
print(fib.running_sum())
print(next(fib))

## Itertools modules => functions that retain property of lazy iterators

from itertools import tee, accumulate

def Fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

s, t = tee(Fibonacci())
pairs = zip(t, accumulate(s))
for _, (fib, total) in zip(range(7), pairs):
    print(fib, total)

## Chaining iterables => exhaust first then begin next

from itertools import chain

chain1 = chain('ABC', 'DEF')
for item in chain1:
    print(item, end=" ")
print("")

chain2 = chain.from_iterable(['ABC', 'DEF'])
for item in chain2:
    print(item, end=" ")
print("")

## Chaining dictionaries

from collections import ChainMap
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
chain = ChainMap(adjustments, baseline)
print(chain.maps)
print(list(chain.keys()))
print(list(chain.values()))
