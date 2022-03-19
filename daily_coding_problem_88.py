"""
This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder.
"""

def divide(dividend,divisor):
    quotient = 0
    sign = 1
    sign2 = 1

    if dividend < 0:
        sign = -1
    if divisor<0:
        sign2 = -1
    divisor = abs(divisor)
    dividend = abs(dividend)
    while dividend>=divisor:
        dividend -= divisor
        quotient+=1
    return sign*quotient*sign2

ans = divide(-10,-4)
print ans