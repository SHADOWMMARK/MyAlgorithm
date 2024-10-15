"""
There are n balls on a table, each ball has a color black or white.

You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

In each step, you can choose two adjacent balls and swap them.

Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

The solution is so gorgeous！！！
"""
class Solution:
  
    def minimumSteps(self, s: str) -> int:
        
        res = 0
        blackCtr = 0
        
        for c in s:
            if c == '0':
                res += blackCtr
            else:
                blackCtr += 1
        
        return res

  # my solution is as below: tring to swap '1' and '0' and add every time the distance
  
      def minimumSteps(self, s: str) -> int:
        ones = s.count('1')
        if ones == 0 or ones == len(s):
            return 0
        first = s.index('1')
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                if i-first > 0:
                    ans += i-first
                    first += 1
                else:
                    return ans
            while (first < len(s) and s[first]!='1'):
                first += 1
        return ans
