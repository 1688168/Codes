class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        """
        * colors[ii]: color @ ii
        * neededTime[ii]: time to remove baloon ii
        * consequtive baloon cannot be same color -> stack
        => min time -> greedy (for consequtive color, remove max time)
        """
        time = 0
        stk = []  # Space: N

        for ii, cc in enumerate(colors):  # Time: N
            # no cost involved when stk is empty or color is diff
            if not stk or (colors[stk[-1][0]] != cc):
                stk.append([ii, cc])
                continue

            flag = True
            # removing the one with lower cost - greedy
            while stk and cc == colors[stk[-1][0]]:
                if neededTime[stk[-1][0]] < neededTime[ii]:
                    time += neededTime[stk[-1][0]]
                    stk.pop()
                else:
                    time += neededTime[ii]
                    flag = False  # current is dropped
                    break
            if flag:  # current is the survival one
                stk.append([ii, cc])

        return time
