from heapq import heappush, heappop, heappushpop


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        starting --target miles--> destination
        stations[i] = [position, fuel]
        """
        curr_fuel = startFuel
        stations.append([target, 0])
        N = len(stations)

        ii = 0
        mxq = []
        cnt = 0
        while ii < N:  # before we reach the end - O(N)
            # have enough fuel to reach the iith station
            if ii < N and curr_fuel >= stations[ii][0]:
                heappush(mxq, -stations[ii][1])
                ii += 1

            else:
                while mxq and curr_fuel < stations[ii][0]:
                    curr_fuel += (heappop(mxq)*-1)
                    cnt += 1

                if curr_fuel < stations[ii][0]:
                    break

        if ii >= N:
            return cnt

        return -1
