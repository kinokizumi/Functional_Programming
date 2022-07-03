#!/usr/bin/python3

########################
#
# This script uses FP to eliminate loops
#
########################

### Ex.1 Single function

def squares(x):
    return x*x

lst = range(5)

for i in lst:
    print(squares(i))

results = list(map(squares, lst))
print(results)

### Ex.2 Sequential functions: use iterables

do_it = lambda f, *args: f(*args)
hello = lambda first, last: print( "Hello", first, last)
bye = lambda first, last: print( "Goodbye", first, last)
list(map(do_it, [hello, bye], ["David", "Dale"], ["Lynch", "Cooper"]))

### Ex.3 Sequential functions: use list comprehension

do_it_all = lambda fns, *args: [list(map(fn, *args)) for fn in fns]
do_it_all([hello, bye], ["David", "Dale"], ["Lynch", "Cooper"])

### Ex.4 Rewrite while loops

## Statement-based while loop

def calc(n):
    while n > 0:
        if n == 5:
            break
        else: 
            print(n*n)
        n -= 1

calc(10)

## FP-style recursive while loop

def while_block(n):
    if n == 5:
        return 1 
    else:
        print(n*n)
    return 0

while_FP = lambda n: (n > 0 and while_block(n)) or while_FP(n-1)
while_FP(10)  

### Ex.5 Remove while loops with useful conditions

## Imperative method

def echo_IMP():
    while 1:
        x = input("IMP -- ")
        if x == "quit":
            break
        else:
            print(x)

echo_IMP()

## FP method -> uses recursion

def identity_print(x):
    print(x)
    return x

echo_FP = lambda: identity_print(input("FP -- ")) == "quit" or echo_FP()
echo_FP()

test
