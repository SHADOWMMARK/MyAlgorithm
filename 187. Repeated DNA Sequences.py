
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
# You may return the answer in any order.


#simple idea is using the sliding windows idea
#get a diction then get every 10-length substr as the key, cnt as the vals if the cnt greater than 1 means the substr occur more than once in the original string
#then we add them into the ans

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        if n <= 10: 
            return []
        m = {}
        for i in range(n):
            cur = s[i:i+10]
            cnt = m.get(cur,0)
            if cnt == 1:
                ans.append(cur)
            m[cur] = cnt+1
        return ans

      
