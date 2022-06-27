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


