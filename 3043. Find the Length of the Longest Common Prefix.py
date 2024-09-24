"""
You are given two arrays with positive integers arr1 and arr2.

A prefix of a positive integer is an integer formed by one or more of its digits, starting from its leftmost digit. For example, 123 is a prefix of the integer 12345, while 234 is not.

A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b. For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

You need to find the length of the longest common prefix between all pairs of integers (x, y) such that x belongs to arr1 and y belongs to arr2.

Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.
"""

class Solution:
    # first find all prefixes of arr1
    # then for each element in arr2, find the longest prefix that is also in arr1
    # the time complexity is O(n*m) where n is the length of arr1 and m is the length of arr2
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pref = set()
        for i in arr1:
            for j in range(1,len(str(i))+1):
                pref.add(str(i)[:j])
        ans = 0
        for i in arr2:
            s = str(i)
            if len(s) <= ans: continue
            for j in range(1,len(s)+1):
                if s[:j] in pref:
                    ans = max(j,ans)

        return ans
