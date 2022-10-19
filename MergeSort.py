arr = [38,27,43,4,20,19,10]
l = 0
r = len(arr)-1
def merge(arr,l,m,r):
    k = m
    while l<=k:
        if arr[l]<=arr[m+1]:
            l+=1
        elif arr[l]>arr[r]:
            arr[l],arr[r] = arr[r],arr[l]
            if l==k:
                r-=1            
        else:
            arr[l],arr[m+1] = arr[m+1],arr[l]
            l+=1
def mergeSort(arr,l,r):
    if l >= r:
        return
    m = l+((r-l)>>1)
    mergeSort(arr,l,m)
    mergeSort(arr,m+1,r)
    merge(arr,l,m,r)
mergeSort(arr,0,len(arr)-1)
print(arr)