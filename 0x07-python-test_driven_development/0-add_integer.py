#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds and returns sum of two numbers

    args:
        a (int): first integer
        b (int): second int
    Raises:
        Type error is raised
    Returns:
        int: returns sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    sum = a + b
    if sum == -float('inf') or sum == float('inf'):
        return 98
    return sum
