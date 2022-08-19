# 15.3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# the idea is to avoid the duplicate in case of running time beyond the limit:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
#         if not nums or len(nums)<3:       #according to describe this can be saved
#             return ans
        for i in range(len(nums)):
            if nums[i] > 0: break   #when the smallest of three bigger than 0 the sum must not = 0
            if i>0 and nums[i-1]==nums[i]:continue  #when the smallest is the same as the last one the finding will be the same
            l = i+1                 #set up two pointer one on two sides of searching area
            r = len(nums)-1
            while l<r:
                Sum = nums[r]+nums[l]+nums[i]
                if Sum==0:      #when sum satisfied add the ans list
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]: 
                        l+=1    #while same digits occur move the pointer in case getting the same result
                    while l<r and nums[r] == nums[r-1]:
                        r-=1
                    l+=1        #if this pair of l,r is satisfied then move on to the next l,r
                    r-=1
                elif Sum>0:     #when sum not satisfied shrink the searching area by adjusting the pointer
                    r-=1
                elif Sum<0: 
                    l+=1       
        return ans
