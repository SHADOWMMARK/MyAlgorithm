# You are given an integer array nums. You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# print(true if you can reach the last index, or false otherwise.

# below is a way not using the dp

nums =[3,2,1,0,4]
def jump(nums):
    n = len(nums)
    if n == 1:
        return True
    i = 0
    maxi = nums[0]
    while i < n-1:
        for j in range(i,maxi+1):
            if j+nums[j]>=n-1:
                return True
            elif j +nums[j]>maxi:
                maxi = j+nums[j]
                i = j
                break
            # let us say when we search until the last one 
            # the maxi is still not enough to reach next element
            if j == maxi and nums[maxi] == 0:
                return False 
        if maxi >= n-1:
            return True

"""
using the dp, make a dp list that store TRUE/FALSE 
to show is the ith element is reachable or not
""" 
def canJump(nums) -> bool:
    n=len(nums)
    dp=[False for _ in range(n)]
    dp[0]=True

    for i in range(n):
        if dp[i]:   # if this position is reachable
            for j in range(1,nums[i]+1):
                if i+j<n:
                    dp[i+j]=True
                if i+j==n-1:
                    return True
    return dp[n-1]