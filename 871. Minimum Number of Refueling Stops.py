    #this is a kind of silly way using dp (with time O(n^2))
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        m = len(stations)
        tempFuel = startFuel
        for index,pos in enumerate(stations):
            if tempFuel < pos[0]:
                return -1
            else:
                tempFuel+=pos[1]
        dp = [startFuel] + [0] * m
        for i in range(m):
            for t in range(i + 1)[::-1]:
                if dp[t] >= stations[i][0]:
                    dp[t + 1] = max(dp[t + 1], dp[t] + stations[i][1])
        for t, d in enumerate(dp):
            if d >= target: return t
        return -1
# using the Priority Queue, O(NlogN) initial res = 0 and in every loop:
# add all reachable stop to priority queue.
# pop out the largest gas from pq and refeul once.
# If can't refuel, means that can not go forward and return -1
    def minRefuelStops(self, target, cur, s):
        pq = []
        res = i = 0
        while cur < target:
            while i < len(s) and s[i][0] <= cur:
                heapq.heappush(pq, -s[i][1])
                i += 1
            if not pq: return -1
            
            cur += -heapq.heappop(pq)
            print(cur)
            res += 1
        return res
