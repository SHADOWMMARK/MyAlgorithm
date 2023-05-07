obstacles = [5,1,5,5,1,3,4,5,1,4]
import bisect
n=len(obstacles)
dp = [1]*n
tempMax = 1
for i in range(1,n):
    x = obstacles[i]
    idx = bisect.bisect_right(obstacles[:i-1], x)
    print(idx,i)
    if idx != 0:
        dp[i] = dp[idx-1] + 1
        
print(dp)