# basic math operation

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
    match int(operation):
        case 1:
            return add(x, y)
        case 2:
            return subtract(x, y)
        case 3:
            return multiply(x, y)
        case _:
            return "Invalid operation"
