#################
# 20231225
#################
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        list of house
        current house depends on prev house

        dp_0: red
        dp_1: green
        dp_2: blue
        0 1 2 ... N-1
        """
        dp_0 = costs[0][0]
        dp_1 = costs[0][1]
        dp_2 = costs[0][2]
        N = len(costs)
        for ii in range(1, N):
            dp_0_tmp = dp_0
            dp_1_tmp = dp_1
            dp_2_tmp = dp_2

            dp_0 = min(dp_1_tmp, dp_2_tmp) + costs[ii][0]
            dp_1 = min(dp_0_tmp, dp_2_tmp) + costs[ii][1]
            dp_2 = min(dp_0_tmp, dp_1_tmp) + costs[ii][2]

        return min(dp_0, dp_1, dp_2)


#########################################

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        dp[ii]: min cost if we paint up to ii 
        """

        N = len(costs)
        red = 0
        blue = 0
        green = 0

        for ii in range(N):
            if ii == 0:
                red = costs[ii][0]
                blue = costs[ii][1]
                green = costs[ii][2]
                continue

            tmp_red = red
            tmp_blue = blue
            tmp_green = green

            red = costs[ii][0] + min(tmp_blue, tmp_green)
            blue = costs[ii][1] + min(tmp_red, tmp_green)
            green = costs[ii][2] + min(tmp_red, tmp_blue)

        return min(red, blue, green)

############################################


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        houses = [[0]*3 for _ in range(n)]
        houses[0] = costs[0]
        for i in range(1, n):
            houses[i][0] = costs[i][0] + min(houses[i-1][1], houses[i-1][2])
            houses[i][1] = costs[i][1] + min(houses[i-1][0], houses[i-1][2])
            houses[i][2] = costs[i][2] + min(houses[i-1][1], houses[i-1][0])

        # print(houses) # see how the costs are progagated

        return min(houses[-1])


##################
# 20231008: this is NOT working. How do you know Greedy is not an good option?
##################
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        Try Greedy, always pick the allowd min -> O(N)
        """
        N = len(costs)

        def find_min(cost, exclude):
            mni = len(cost)
            mnv = math.inf
            for ii, vv in enumerate(cost):
                if exclude is not None and ii == exclude:
                    continue
                if vv < mnv:
                    mni = ii
                    mnv = vv

            return mni, mnv

        ttl = 0
        for ii in range(N):
            if ii == 0:
                exclude = None
            mi, mc = find_min(costs[ii], exclude)
            exclude = mi
            ttl += mc

        return ttl
