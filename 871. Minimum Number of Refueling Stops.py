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
