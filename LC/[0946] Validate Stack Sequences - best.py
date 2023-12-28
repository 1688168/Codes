################
# 20231228
################
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        M, N = len(pushed), len(popped)
        stk = []
        jj = 0
        for ii, push in enumerate(pushed):
            stk.append(push)

            while stk and stk[-1] == popped[jj]:
                stk.pop()
                jj += 1

        return not stk


########################
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        N = len(pushed)
        M = len(popped)
        jj = 0
        stk = []
        for ii, vv in enumerate(pushed):
            stk.append(vv)

            while jj < M and stk and popped[jj] == stk[-1]:
                stk.pop()
                jj += 1

        return jj == M
