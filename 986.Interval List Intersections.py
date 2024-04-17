##LEETCODE 986
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
# Return the intersection of these two interval lists.
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

##THE idea of sloving the problem is define two pointer pointing two end of an intervel and by comparing the different conditions then output all overlapping parts.
#idea is simple but should pay attention to the conditions.
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m,n = len(firstList), len(secondList)
        i,j = 0,0
        ans = []
        while i<m and j<n:
            la, ra = firstList[i][0], firstList[i][1]
            lb, rb = secondList[j][0], secondList[j][1]
            if ra<lb: i += 1
            elif rb<la: j += 1
            elif lb==ra:
                ans.append([lb,ra])
                i+=1
            elif la==rb:
                ans.append([la,rb])
                j+=1
            elif lb<=la and rb <=ra:
                ans.append([la,rb])
                j+=1
            elif lb<=la and rb >=ra:
                ans.append([la,ra])
                i+=1
            elif la<=lb and ra <=rb:
                ans.append([lb,ra])
                i+=1
            elif la<=lb and ra >=rb:
                ans.append([lb,rb])
                j+=1
        return ans
                
        
