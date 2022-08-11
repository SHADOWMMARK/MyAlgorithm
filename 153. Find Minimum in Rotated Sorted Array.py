class Solution:
  #two seperate way, one is rotated one is the sorted, and use binary search
    def findMin(self, nums: List[int]) -> int:
        if nums[0]>nums[-1]:
            # if len(nums)<=2:
            #     return nums[-1]
            l = 0
            r = len(nums)-1
            while l < r:
                mid = l+((r-l)>>1)
                temp = nums[mid]
                if temp>=nums[l] and temp>nums[r]:
                    l = mid+1
                elif temp<nums[r]:
                    r = mid

            return nums[l]
                    
        else:
            return nums[0]
