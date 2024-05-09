def maximumHappinessSum(self, hap: List[int], k: int) -> int:
    ans = 0
    hap.sort()
    i = 0
    while hap and hap[0]>0 and k>0:
        k-=1
        ans += hap.pop(-1)-i
        i+=1
    return ans
