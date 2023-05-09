import bisect
# li = [[10,'1'],[20,'2']]
# print(bisect.bisect(li,[10]))
# l = [10,15]
# print(bisect.bisect(l,10))

intervals = [2,3,5]
intervals.sort()
print(bisect.bisect_left(intervals,6))