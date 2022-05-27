""" both python2 and python3 have the round() function
but I found that using the round(1.5) and round(2.5) in python 3 all get the result 2;
this is because to make statistics fairer, and lower the error of rounding 
in python3 the function round is not 'strict' rounding (when arrive 5 then become 10)
now it depends on higher bit, if the higher bit is a odd then add 1 otherwise will not, so the round(1.5)=round(2.5)==6"""

#here is a way in python3 to get a 'strict' rounding

from decimal import Decimal     #here is some example using the decimal, it will help get more accuracy

"""The decimal module was designed to support “without prejudice, both exact unrounded decimal arithmetic 
(sometimes called fixed-point arithmetic) and rounded floating-point arithmetic.” 
– excerpt from the decimal arithmetic specification."""

print(0.29 * 100)  # 28.999999999999996
print(Decimal(0.29) * 100)  # 28.99999999999999800159855567
print(Decimal('0.29') * 100)  # 29.00
print(Decimal('1.5093').quantize(Decimal('1.00')))  # 1.51

def round(number, ndigits=None):
    
    exp = Decimal('1.{}'.format(ndigits * '0')) if ndigits else Decimal('1')
    return type(number)(Decimal(number).quantize(exp, ROUND_HALF_UP)) 

# if here ROUND_HALF_UP set to be ROUND_HALF_DOWN OR ROUND_DOWN OR ROUND_UP
# Decimal('7.325').quantize(Decimal('.01'), rounding=XX) will be 7.33, 7.32, 7.32 and 7.33
