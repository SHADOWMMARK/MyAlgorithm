# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


##create two list recording the left all and the right all product of a entry in the original one

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lproduct = [1]
        rproduct = [1]
        n = len(nums)
        rnums = nums[::-1]
        for i in range(n-1):
            lproduct.append(lproduct[-1]*nums[i])
            rproduct.append(rproduct[-1]*rnums[i])
        rproduct[:] = rproduct[::-1]
        ans = []
        for i in range(n):
            ans.append(lproduct[i]*rproduct[i])
        return ans 
