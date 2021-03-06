import numpy as np
import types
import numbers.Number

# Task 1

a = 8
b = 8
c = 2.0

assert a == b, 'a should be equal to b.'
assert a % c == 0, 'a should be a multiple of c.'
assert b == c**3, 'b should be the cube of c.'
assert c != 3, 'c should not be equal to 3.'
assert isinstance(b, int), 'b should be an int.'
assert isinstance(c, float), 'c should be a float.'


# Task 2

def bisection(F, a, b, tol):
    '''
    Finds the root of F in the interval [a, b] using
    the bisection method, to within an error of tol.
    '''
    assert isinstance(f, types.FunctionType), 'F should be a function'
    assert isinstance(a, Number), 'a should be a number'
    assert isinstance(b, Number), 'b should be a number'
    assert a < b, 'a should be less than b'
    assert isinstance(tol, Number), 'tol should be a number'
    assert tol > 0, 'tol should be greater than zero'
    # Iteration count
    its = 0

    # Midpoint
    c = 0.5 * (a + b)
    
    # Loop until the root is found
    while abs(F(c)) >= tol:
        # Increment the iteration count
        its += 1

        if F(a) * F(c) <= 0.0:    # F(a) and F(c) have different signs (or one or both is zero) ...
            b = c                 # ... a root is between a and c (or equals a or c)
        else:
            a = c                 # Else, a root is between c and b (or equals b)

        # Find the next midpoint
        c = 0.5 * (a + b)
    
    # Return the root and the number of iterations
    return c, its

def f(x):
    return np.sin(x) + 1

bisection(f, f, 0.5, 1e-8)

