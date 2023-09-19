"""
notice that there is a very important equation
x^^n when n is even: = (x*x)^^(n//2)
                odd: = x(x*x)^^((n-1)//2)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:

        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()
        
        return float(f) if n >= 0 else 1/f