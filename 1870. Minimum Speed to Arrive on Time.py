import math
def minSpeedOnTime(dist, hour: float) -> int:

    if hour <= len(dist)-1:
        return -1
    l,r = 1, max(dist) #here the question happend! should set the r towards 1000000
    while l < r:
        mid = r+(l-r)//2
        if sum(math.ceil(a/mid) for a in dist[:-1]) + dist[-1]/mid > hour:
            l = mid + 1
        else:
            r = mid
    print(l,r)
    return r
