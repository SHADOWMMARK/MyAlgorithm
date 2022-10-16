import imp


import collections
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cVal = collections.Counter(s).values()
        od = 0
        for item in cVal:
            if item % 2 != 0:
                od += 1
        print(od)
        if od <= 1:
            return len(s)
        else:
            return len(s) - od + 1