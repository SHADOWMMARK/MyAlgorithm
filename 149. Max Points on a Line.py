# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def calculateK(x1,y1,x2,y2):
            return (y1-y2)*1.0/(x1-x2)
        ans = 0
        m = len(points)
        for i in range(m):
            d = {"i":1}
            same = 0
            for j in range(i+1,m):
                x1,x2,y1,y2 = points[i][0],points[j][0],points[i][1],points[j][1]
                if x1==x2 and y1==y2:
                    same+=1
                    continue
                if x1==x2: k = "i"
                else: k = calculateK(x1,y1,x2,y2)
                if k not in d: d[k]=1
                d[k]+=1
            ans = max(ans,max(d.values())+same)
        return ans
                
    # def maxPoints(self, points):
    #     l = len(points)
    #     m = 0
    #     for i in range(l):
    #         dic = {'i': 1}
    #         same = 0
    #         for j in range(i+1, l):
    #             tx, ty = points[j][0], points[j][1]
    #             if tx == points[i][0] and ty == points[i][1]: 
    #                 same += 1
    #                 continue
    #             if points[i][0] == tx: slope = 'i'
    #             else:slope = (points[i][1]-ty) * 1.0 /(points[i][0]-tx)
    #             if slope not in dic: dic[slope] = 1
    #             dic[slope] += 1
    #         m = max(m, max(dic.values()) + same)
    #     return m