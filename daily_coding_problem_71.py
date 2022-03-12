"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability,
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

def foo():
    # some random code
    return 0

def rand():
    i = 0
    i = 5*foo() + (foo() - 5)
    if i<22:
        if i<0:
            return (i%7-7) +1
        else:
            return (i%7) +1
    return rand()

ans = rand()
print ans
