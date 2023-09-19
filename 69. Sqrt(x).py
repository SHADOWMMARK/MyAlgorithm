"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
esay binary search
"""

def mySqrt(self, x: int) -> int:
    l,r = 0,x

    while r >= l:
        m = (l+r)//2
        if m*m<x:
            l = m + 1
        elif m*m==x:
            return m
        else:
            r = m - 1
    return r
