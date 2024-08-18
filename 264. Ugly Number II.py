"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.
"""
import heapq
def nthUglyNumber(self, n: int) -> int:
    if n == 1:
        return 1
    que = [1]
    factors = [2,3,5]
    seen = set(que)

    for _ in range(n):
        small = heapq.heappop(que)
        for f in factors:
            new = small * f
            if new not in seen:
                seen.add(new)
                heapq.heappush(que, new)
    
    return small

# Time complexity: O(nlogn)
# Space complexity: O(n)

#ty for tips from : @_Vietnamese_
"""
One approach without DP is using Heap with the intuition as follow:

The next 3 potential ugly numbers are:

smallest number in the heap * 2
smallest number in the heap * 3
smallest number in the heap *5
For example, we start with a heap = [1], the next 3 candidates are: [2,3,5]. We remove 1 because it has already been used to generate the future values. Now, the smallest number in the heap is 2. We can use this one to generate the potential candidates, which are [4,6,10].

Hope this intuition help!
"""