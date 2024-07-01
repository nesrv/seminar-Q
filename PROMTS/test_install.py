
def get_max_value(a,b,c):
    """
    Returns the maximum value among the three given integers.
    """
    return max(a, b, c)


def get_max_value(a, b, c):
    """
    Returns the maximum value among the three given integers.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

