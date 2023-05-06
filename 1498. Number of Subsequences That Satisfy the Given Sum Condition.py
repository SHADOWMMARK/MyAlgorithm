def numSubseq(nums, target: int) -> int:
    ans = 0
    n = len(nums)

    temp = [nums[0]]
    for i in range(n):
        mi,mx = nums[i],nums[i]
        if mi + mx <= target:
            ans += 1
            temp = [nums[i]]
        else:
            break
        for j in range(i+1,n):
            nw = nums[j]
            mi = min(mi,nw)
            mx = max(mx,nw)
            if mi + mx <= target:
                temp.append(nw)
            else:
                k = len(temp)
                ans += 2**(k-1)
                break
    return ans
nums = [3,3,6,8]
t = 10
print(numSubseq(nums,t))

# this will cause TLE, while using two sum's idea will be fine
# Correct idea is the order do not matter! so we could firstly sort it
# For example: 

def numS(nums, t):
    nums.sort()
    ans = 0
    n = len(nums)
    end = n - 1
    for i in range(n):
        while nums[i]+nums[end] > t:
            if end > i:
                end -= 1
            else:
                return ans % (10**(9)+7)
        ans += 2**(end-i)
    return ans % (10**(9)+7)