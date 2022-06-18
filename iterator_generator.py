#!/usr/bin/python3

####### Use build-in functions to create iterator #######

value = "Bitcoin"
it = iter(value)
print(next(it))
print(next(it))
print(next(it), '\n')


####### Define an iterator class #######

class Reverse:

    def __init__(self, value):
        self.val = value
        self.index = len(value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.val[self.index]

######## Test iterator #########

item = Reverse("Bitcoin")
for char in item:
    print(char)

####### Define a generator #######

def reverse(value):
    for index in range(len(value)-1, -1, -1):
        yield value[index]

######## Test generator #########

for char in reverse("Bitcoin"):
    print(char)

print(list(reverse("Bitcoin")))

######## List comprehension ########

data = [2, 1, 0, -1, -2]
power = [x**2 for x in data]
print(power)

power = (x**2 for x in data)
print(list(power)) 
