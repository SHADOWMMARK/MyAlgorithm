import bisect
def LOCAEP(nums):
    reco = []
    for i,x in enumerate(nums):
        if not reco or reco[-1]<=x:
            reco.append(x)
            nums[i] = len(reco)
        else:
            idx = bisect.bisect(reco,x)
            reco[idx] = x
            nums[i] = idx + 1
    return nums
print(LOCAEP([3,1,5,6,4,2]))