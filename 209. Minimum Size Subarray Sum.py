# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

# using the idea of sliding windows:

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if sum(nums)<target: return 0
        n = len(nums)
        l, r =0, 1
        s = nums[l]
        ans = 10e9
        while r < n:
            while s<target and r < n:
                s += nums[r]
                r += 1
            while s>=target and l<r:
                s -= nums[l]
                l += 1
            ans = min(r-l+1,ans)
        return ans
    def minSubArrayLen(self, target: int, nums) -> int:
        if t>sum(nums):
            return 0
        l = 0
        s = 0
        ans = len(nums)
        for r,val in enumerate(nums):
            s+=val
            if s<t:
                continue
            else:
                for i in range(l,r+1):
                    if s-nums[i] < t:
                        break
                    else:
                        s-=nums[i]
                        l+=1
            ans = min(r-l+1,ans)
        return ans