class Solution:
  
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vw = [] #use prefix_sum to record
        cnt = 0
        vws = {'a', 'e', 'i', 'o', 'u'}
        for idx, word in enumerate(words):
            if word[0] in vws and word[-1] in vws:
                cnt += 1
            vw.append(cnt)
        ans = []
        for st,ed in queries:
            if st == 0:
                cnt = vw[ed]
            else:
                cnt = vw[ed]-vw[st-1]
            ans.append(cnt)
        return ans
