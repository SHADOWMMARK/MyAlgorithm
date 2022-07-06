def longestConsecutive(self, nums: List[int]) -> int:
    if not nums:
        return 0
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    ans = 1
    temp = 1
    if len(nums) == 1:
        return 1
    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]+1:
            temp += 1
        else:
            if temp > ans:
                ans = temp
            temp = 1
    if temp > ans:
        ans = temp
    return ans
