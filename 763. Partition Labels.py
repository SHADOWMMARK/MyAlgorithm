# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.
# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.
# Return a list of integers representing the size of these parts.

#idea: find every chr's possible area [l,r] then merge the areas if they are overlapping.


# The enumerate() function is used to combine a traversable data object (such as a list, tuple or string) into an index sequence,
# and list the data and data subscripts at the same time, generally used in for loops

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        LastPosition = {s: index for index, s in enumerate(S)} # this is tricky that it will record every last positon of every chr in s (for if there are different value in
                                                       # of same key that the latter postion will take place privious one!)
        tempR = LastPosition[s[0]]
        cnt = 0
        ans = []
        for i in range(len(s)):
            cnt+=1
            if LastPosition[s[i]]>tempR:      # if the chr here need more "space" then we should broaden our space(by move our tempR right more)
                tempR = LastPosition[s[i]]
            if i == tempR:                    # if here we go over the area and find there is no more space conflict then we append this area's length
                ans.append(cnt)
                cnt = 0
        return ans
