class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x<4:
            return 1
        l,r = 0,x//2
        while l < r:
            mid = l+((r-l)>>1)
            temp = mid ** 2
            if temp>x:
                r = mid - 1
            elif (mid+1)>x/(mid+1):                   #this line is awesome!
                return mid
            else:
                l = mid +1
        return l
