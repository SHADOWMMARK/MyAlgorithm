# Given an integer array nums, return the length of the longest strictly increasing
def LIS(nums):
    n = len(nums)
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
    return max(dp)
#dp: longest length end with idx i nums element