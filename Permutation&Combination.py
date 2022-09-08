# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.    
  
  def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        numsLeft = []
        for i in nums:
            numsLeft.append(i)
        ans = []
        def helper(nums,numsLeft):
            if len(nums)==n :
                ans.append(nums)
                return 
            for i in range(len(numsLeft)):
                num = numsLeft[i]
                helper(nums+[num],numsLeft[i+1:]+numsLeft[:i])
        helper([],numsLeft)
        return ans
      
# 77. Combinations
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        numsLeft = []
        for i in range(n):
            numsLeft.append(i+1)
        ans = []
        def helper(nums,k,numsLeft):
            if k == 0 :
                ans.append(nums)
                return 
            for i in range(len(numsLeft)):
                num = numsLeft[i]
                helper(nums+[num],k-1,numsLeft[i+1:])
        helper([],k,numsLeft)
        return ans
