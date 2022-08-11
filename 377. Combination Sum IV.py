class Solution:
  #this is a bottom-up solution
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0]*(target+1)
        dp[0]=1
        for i in range(target+1):
            for index,a in enumerate(nums):
                if i - a>=0:
                    dp[i]+=dp[i-a]
        print(dp)
        return dp[target]
  #this is a top-down solution
