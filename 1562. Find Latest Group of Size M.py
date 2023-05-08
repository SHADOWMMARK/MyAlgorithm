def findLatestStep(arr, m: int) -> int:
    n = len(arr)
    if n == m:
        return m
    length = [0]*(n+2)
    ans = -1
    for i, x in enumerate(arr):
        left,right = length[x-1],length[x+1]
        if left == m or right == m:
            ans = i
        length[x-left]=length[x+right]=left+right+1
    print(length)
    return ans
print(findLatestStep([3,5,1,2,4],1))
