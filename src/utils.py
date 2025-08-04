from typing import Optional
import numpy as np

# TODO: make all functions work with strings as well
# TODO: add a new cool calculator function

def sum(a: int, b: int) -> int:
    '''
    This function returns the sum of two numbers

    Args:
    a: float the first number
    b: float the second number

    Returns:
    float the sum of a and b
    '''
    return a + b

def sum(c: int, d: int) -> int:
    return c + d 

def multiply(a, b) -> float:
    '''
    This function returns the product of two numbers

    Args:
    a: float the first number
    b: float the second number

    Returns:
    float
    '''
    return a * b

def divide(a: [int, float, str] ,  b:  [int, float, str]) -> float:
    '''
    Divides two numbers, accepting float, int, or numeric strings.

    Args:
    a: float , int , str - the number to be divided
    b: float , int , str - the divisor

    Returns:
    float - the result of the division

    Raises:
    ValueError: if inputs cannot be converted to float or division by zero occurs
    '''
    try: 
        b = float(b)
    except:
        raise ValueError("input b can't be interpreted as a number")
    try:
        return float(a) / float(b)
    except:
        raise ZeroDivisionError

def modulo(a: [int, str, float], b: [int, str, float]):
    '''
    Args:
    a: int the number to be divided
    b: int the divisor

    Returns: float
    '''

    # I think this could be made more efficient?
    result = a - (np.floor(a / b) * b)

    return result

def element_wise_multiply(a: np.array, b: np.array) -> np.array:
    '''
    Args:
    a: np.array
    b: np.array

    Returns:
    np.array
    '''
    # let's hope that both vectors have the same shape

    if a.shape==b.shape:

        return np.multiply(a, b)
    else:
        raise ValueError
    

def return_hexadecimal(a: int) -> float:
    '''

    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return hex(a)


def return_random_number() -> int:
    '''
    Args:
    a: float
    b: float

    Returns:
    float
    '''

    return np.random.randint(0, 50)