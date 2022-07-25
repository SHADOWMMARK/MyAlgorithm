#python version of this commit: https://leetcode.com/problems/task-scheduler/discuss/104500/Java-O(n)-time-O(1)-space-1-pass-no-sorting-solution-with-detailed-explanation
def leastInterval(self, tasks: List[str], n: int) -> int:
    C = collections.Counter(tasks)
    CC = sorted(C.items(),key=lambda x:x[1],reverse = True)
    mostFrequency = CC[0][1]
    k=0
    for i in range(len(CC)):
        if CC[i][1]==mostFrequency:
            k+=1
        else:
            break
    parts = mostFrequency-1
    empty = parts*(n-(k-1))
    avaliable = len(tasks)-mostFrequency*k
    idles = max(0,empty-avaliable)
    return len(tasks)+idles
