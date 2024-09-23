"""
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.
"""
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        up_bound = len(s)
        dp = [up_bound]*(len(s)+1)
        dp[0] = 0
        for i in range(1,len(s)+1):
            dp[i] = dp[i-1]+1
            for j in range(1,i+1):
                if s[i-j:i] in dictionary:
                    dp[i] = min(dp[i],dp[i-j])
        return dp[-1]