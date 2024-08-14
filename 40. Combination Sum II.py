"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""
def combination2(candidates:list[int],target:int) -> list[list[int]]:
    candidates.sort()
    st = [(0,0,[])]
    res = []
    while st:
        idx, sum, path = st.pop()
        if sum == target:
            res.append(path)
            continue
        for i in range(idx,len(candidates)):
            if i > idx and candidates[i] == candidates[i-1]:    # skip duplicates
                continue
            if sum + candidates[i] > target:
                break
            st.append((i+1,sum+candidates[i],path+[candidates[i]]))
    return res
print(combination2([10,1,2,7,6,1,5],8)) # [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]