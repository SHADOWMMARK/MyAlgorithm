"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

class Solution:
    def sortedSquares(self, nums) -> list[int]:
        ans = sorted(nums,key = lambda x:abs(x))
        return [i**2 for i in ans]