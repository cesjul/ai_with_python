def sum(a, b):
    return a + b

def multi(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Can`t divide by zero')
    
    return a / b

def sub(a, b):
    return a - b

def module(a):
    return a % 2