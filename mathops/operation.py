from enum import Enum
# basic math operation

class operations(Enum):
    addition = 1
    subtraction = 2
    mulipication = 3

def add(x, y):
    """ add y to x """
    return x + y


def subtract(x, y):
    """ subtract y from x"""
    return x - y


def multiply(x, y):
    """ Multiply x and y"""
    return x * y


def operate(operation, x, y):
    """ look at the operation number and determine which one to use"""
    x = int(x)
    y = int(y)
    operation = operations[operation].value
    match int(operation):
        case operations.addition.value:
            return add(x, y)
        case operations.subtraction.value:
            return subtract(x, y)
        case operations.mulipication.value:
            return multiply(x, y)
        case _:
            return "Invalid operation"
