"""
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.

"""

def power(x,y):
    if y == 0:
        return 1
    temp = power(x,int(y/2))
    if y%2 == 0:
        return temp*temp
    else:
        return x*temp*temp

ans = power(4,200000)
print(ans)
