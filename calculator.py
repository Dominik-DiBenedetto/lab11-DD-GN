"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b

def mul(a, b): 
    return a * b

def div(a, b): 
    if a == 0: raise ZeroDivisionError()
    return b / a

def log(a, b):
    if b <= 0: raise ValueError("b must be > 0")
    if a <= 0: raise ValueError("a must be 1 or greater")
    return math.log(b,a)

def exp(a, b): 
    return a**b
