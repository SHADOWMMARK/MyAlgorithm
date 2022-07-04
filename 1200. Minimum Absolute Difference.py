# Think the thing should mention is that should rearrange the arr at the first
# so do not need the abs() function
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l = len(arr)
        arr.sort()
        gap = arr[1]-arr[0]

        if l == 2:
            return [[arr[0],arr[1]]]
        
        ans = []
        for i in range(l-1):
            if arr[i+1]-arr[i]>gap:
                continue
            elif arr[i+1]-arr[i]<gap:
                ans = []
                ans.append([arr[i],arr[i+1]])
                gap = arr[i+1]-arr[i]
            else:
                ans.append([arr[i],arr[i+1]])
        
        return ans
