#easy prob, direct idea is using the hash table to record, then if some item in nums occur twice then return it
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        h ={}
        for i in nums:
            if i in h:
                return i
            else:
                 h[i]=1
# but there is an interesting idea I pick up at the leetcode: it is based on the Principle of inclusion-exclusion
# basic idea is when a circle with 2n number place and should place n balls the only condition that those ball 
# are not adjacent is that the ball and blank occur intermittently.
# the idea is when the special item place intermittently with a non-special number : such as  1 3 1 4 1 5 1 6 ... 
# so we check all 3 neighbering items of the array then there must come 2 out of 3 are the same.
# then we should get remainder to let the array become circle.

