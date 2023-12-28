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
