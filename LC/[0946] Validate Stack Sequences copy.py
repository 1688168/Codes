##############
# 20231105
##############
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        M = len(pushed)
        N = len(popped)

        stk = []
        jj = 0
        for ii, pop in enumerate(popped):
            if stk and stk[-1] == pop:
                stk.pop()
                continue
            while jj < M and pushed[jj] != pop:
                stk.append(pushed[jj])
                jj += 1

            jj += 1

        return len(stk) == 0

##############################


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        - simulate the process according to popped
        - numbers are unique in each list
        - O(N)
        """

        N = len(popped)
        M = len(pushed)
        jj = 0
        my_pushed = []
        for ii in range(N):
            curr = popped[ii]
            if my_pushed and my_pushed[-1] == curr:
                my_pushed.pop()
                continue

            while jj < M and pushed[jj] != curr:
                my_pushed.append(pushed[jj])
                jj += 1

            if jj >= N:
                return False
            jj += 1

        return True
