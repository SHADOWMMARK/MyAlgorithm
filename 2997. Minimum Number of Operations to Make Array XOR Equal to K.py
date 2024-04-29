def minOperations(self, nums: List[int], k: int) -> int:
    ans = reduce(xor,nums)
    return bin(ans^k).count('1')