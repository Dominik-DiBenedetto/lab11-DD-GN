# https://github.com/Dominik-DiBenedetto/lab11-DD-GN
# Partner 1: Gavin Nazal
# Partner 2: Dominik DiBenedetto

import math

def square_root(a):
    if a < 0:
        raise ValueError()
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b) # can have negative nums

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError()
    return math.log(b, a)

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0: raise ZeroDivisionError()
    return b / a

def exp(a, b): 
    return a**b

