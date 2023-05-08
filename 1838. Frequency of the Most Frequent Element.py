# The frequency of an element is the number of times it occurs in an array.

# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

# Return the maximum possible frequency of an element after performing at most k operations.
def maxFrequency( A, k):
    i = 0
    A.sort()
    for j in range(len(A)):
        k += A[j]
        if k < A[j] * (j - i + 1):
            k -= A[i]
            i += 1
    return j - i + 1
print(maxFrequency([1,4,8,13],5))