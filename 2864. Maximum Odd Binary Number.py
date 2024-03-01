"""
You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.
"""
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        n = len(s)
        if ones == 1:
            return '0'*(n-1)+'1'
        ans = ''
        
        for i in range(ones-1):
            ans += '1'
        for i in range(n-ones):
            ans += '0'

        return ans+'1'
    
    
    """
    The above solution is not optimal, we can simply count the number of ones and zeros and return the string as follows:
    """
    def maximumOddBinaryNumber(self, s: str) -> str:
        return '1'*(s.count('1')-1)+ '0'*(len(s)-s.count('1'))+'1'