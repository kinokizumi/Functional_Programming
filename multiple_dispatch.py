#!/usr/bin/python3

##############
#
# This script gives examples of multiple dispatch: programming multiple paths of execution
#
##############

## Game of Rock, Paper, Scissors

class Thing(object): pass
class Rock(Thing): pass
class Paper(Thing): pass
class Scissors(Thing): pass

## Imperative approach

def beats(x, y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None
        elif isinstance(y, Paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Paper):
        if isinstance(y, Rock):
            return x
        elif isinstance(y, Paper):
            return None
        elif isinstance(y, Scissors):
            return y
        else:
            raise TypeError("Unknown second thing")
    elif isinstance(x, Scissors):
        if isinstance(y, Rock):
            return y
        elif isinstance(y, Paper):
            return x
        elif isinstance(y, Scissors):
            return None
        else:
            raise TypeError("Unknown second thing")
    else:
        raise TypeError("Unknown first thing")

rock, paper, scissors = Rock(), Paper(), Scissors()

print(beats(paper, rock))
#beats(paper, 3)

## Object-oriented: delegate dispatch to the object

## Duck typing -> an object is of a given type if it has all methods and properties required

class DuckRock(Rock):
    def beats(self, other):
        if isinstance(other, Rock):
            return None
        elif isinstance(other, Paper):
            return other
        elif isinstance(other, Scissors):
            return self
        else:
            raise TypeError("Unknown second thing")

class DuckPaper(Paper):
    def beats(self, other):
        if isinstance(other, Rock):
            return self
        elif isinstance(other, Paper):
            return None
        elif isinstance(other, Scissors):
            return other
        else:
            raise TypeError("Unknown second thing")

class DuckScissors(Scissors):
    def beats(self, other):
        if isinstance(other, Rock):
            return other
        elif isinstance(other, Paper):
            return self
        elif isinstance(other, Scissors):
            return None
        else:
            raise TypeError("Unknown second thing")

def beats2(x, y):
    if hasattr(x, 'beats'):
        return x.beats(y)
    else:
        raise TypeError("Unknown first thing")

rock, paper, scissors = DuckRock(), DuckPaper(), DuckScissors()
print(beats2(rock, paper))
#beats2(3, rock)

## Pattern matching: define different cases

from multipledispatch import dispatch

@dispatch(Rock, Rock)
def beats3(x, y): return None

@dispatch(Rock, Paper)
def beats3(x, y): return y

@dispatch(Rock, Scissors)
def beats3(x, y): return x

@dispatch(Paper, Rock)
def beats3(x, y): return x

@dispatch(Paper, Paper)
def beats3(x, y): return None

@dispatch(Paper, Scissors)
def beats3(x, y): return y

@dispatch(Scissors, Rock)
def beats3(x, y): return y

@dispatch(Scissors, Paper)
def beats3(x, y): return x

@dispatch(Scissors, Scissors)
def beats3(x, y): return None

@dispatch(object, object)
def beats3(x, y):
    if not isinstance(x, (Rock, Paper, Scissors)):
        raise TypeError("Unknown first thing")
    else:
        raise TypeError("Unknown second thing")

rock, paper, scissors = Rock(), Paper(), Scissors()
print(beats3(rock, paper))
#beats3(rock, 3)
