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
                
        