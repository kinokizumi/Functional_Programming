#!/usr/bin/python3

############
#
# This script experiments with some higher-order functions: take functions as arguments & return a function as result
#
############

## Basics

## reduce: takes successive items of an iterable then combines them in some way

from functools import reduce
import operator

print( sum(range(10)) )
print( reduce(lambda a, b: a+b, range(10), 0) )
print( reduce(operator.add, range(10), 0) )        # faster & cleaner with operator module

## map(func, iter) == (func(x) for x in iter) 

add5 = lambda n: n+5
print( list(map(add5, range(10))) )
print( reduce(lambda l, x: l+[add5(x)], range(10), []) )

## filter(func, iter) == (x for x in iter if func(x))

isOdd = lambda n: n%2
print( list(filter(isOdd, range(10))) )
print( reduce(lambda l, x: l+[x] if isOdd(x) else l, range(10), []) )

## Utility HOF

## compose: return application of functions to a data argument

def compose(*funcs):
    """Return a new function s.t. compose(f,g,...)(x) == f(g(...(x))) """
    def inner(data, funcs=funcs):
        result = data
        for f in reversed(funcs):
            result = f(result)
        return result
    return inner

times2 = lambda x: x*2
minus3 = lambda x: x-3
mod6 = lambda x: x%6
f = compose(mod6, times2, minus3)
print( all( f(i)==((i-3)*2)%6 for i in range(10000) ) )

## all/any: useful to check data properties

from functools import partial       # prefill a nb of arguments for a given func

all_pred = lambda item, *tests: all(p(item) for p in tests)
any_pred = lambda item, *tests: any(p(item) for p in tests)

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            return False
    return True 

is_lt100 = partial(operator.ge, 100)
is_gt10 = partial(operator.le, 10)

print( all_pred(71, is_lt100, is_gt10, is_prime) )
predicates = (is_lt100, is_gt10, is_prime)
print( all_pred(107, *predicates) )

## juxt: call functions with same arguments & return a tuple of results

from toolz.functoolz import juxt

print( juxt(is_lt100, is_gt10, is_prime)(71) )
print( all( juxt(is_lt100, is_gt10, is_prime)(71) ) )
print( juxt(is_lt100, is_gt10, is_prime)(101) )

