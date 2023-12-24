##############
# 20231224
##############
from heapq import heappush, heappop, heappushpop
from heapq import heappush, heappop, heappushpop, heapify


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        stations = [[0, 0]]+stations
        cnt = 0
        """
        Greedy: each time we need refueling, refueling the earlier max gas station
        """
        curr_fuel = startFuel
        mxh = []

        for ii, gg in stations:

            while mxh and curr_fuel < ii:
                g, idx = heappop(mxh)
                curr_fuel += (-g)
                cnt += 1
            heappush(mxh, [-1*gg, ii])
            if curr_fuel < ii:
                return -1

        # print("curr_fuel: ", curr_fuel, " cnt: ", cnt)
        return cnt if curr_fuel >= target else -1

#####################


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
