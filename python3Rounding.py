""" both python2 and python3 have the round() function
but I found that using the round(1.5) and round(2.5) in python 3 all get the result 2;
this is because to make statistics fairer, and lower the error of rounding 
in python3 the function round is not 'strict' rounding (when arrive 5 then become 10)
now it depends on higher bit, if the higher bit is a odd then add 1 otherwise will not, so the round(1.5)=round(2.5)==6"""

#here is a way in python3 to get a 'strict' rounding

def round(number, ndigits=None):
    
    exp = Decimal('1.{}'.format(ndigits * '0')) if ndigits else Decimal('1')
    return type(number)(Decimal(number).quantize(exp, ROUND_HALF_UP))
