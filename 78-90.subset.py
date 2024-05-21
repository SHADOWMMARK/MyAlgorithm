# 90's version is built on 78's, only getting rid of the duplicated one.
#78
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        return res
    def subsets2(self, nums):
        ans = [[]]
        for num in nums:
            ans += [item + [num] for item in ans]
        return ans
    
#90
class Solution90(object):
    def subsetsWithDup(self, nums):

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1,tmp + [nums[j]] )
        helper(0, [])
        ans = []
        for item in res:
            item.sort()
            if not item in ans:
                ans.append(item)
        return ans
#78 using the binary code to define every set:
# for example 0000 for the 1,2,3,4 entries
# 0001 stands for only get the 1, 0010 stands for getting the 2 only:
'''
    public static List<List<Integer>> binaryBit(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        for (int i = 0; i < (1 << nums.length); i++) {
            List<Integer> sub = new ArrayList<Integer>();
            for (int j = 0; j < nums.length; j++)
                if (((i >> j) & 1) == 1) sub.add(nums[j]);
            res.add(sub);
        }
        return res;
    }
here is a really brilliant code:
it is not from myself but it is really amazing!!!
this seems not using the idea of recursion.
        res = [[]]
        for item in nums:
            res = res + [[item]+num for num in res] ##when I understand this line, it really shock me!
        return res

'''
newClass = Solution()
print(newClass.subsets2([1,2,3]))