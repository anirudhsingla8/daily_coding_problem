"""
This problem was asked by Jane Street.
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
"""

def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair

def car(f):
    z = lambda x, y: x
    return f(z)

def cdr(f):
    z = lambda x, y: y
    return f(z)


pair = cons(1,2)
print(car(pair))
print(cdr(pair))