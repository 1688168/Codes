class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        * validating something moving back/forth -> stack
        * push until we have first pop
        1. traverse each element of popped
        -- if same as top of stk -> pop stk and continue
        -- else: 
           keep adding elements from pushed to stk
        """
        M = len(pushed)
        N = len(popped)
        jj = 0
        stk = []
        for ii, pop in enumerate(popped):  # will get out with determined scope
            # print("ii: ", ii, " jj: ", jj, " stk: ", stk, " pop: ", pop)
            if stk and stk[-1] == pop:
                stk.pop()
                continue
            while jj < M and (not stk or stk[-1] != pop):

                stk.append(pushed[jj])
                jj += 1
            # now we have stk[-1]==pop
            if stk and stk[-1] == pop:
                stk.pop()

        # print("--> ii: ", ii, " jj: ", jj, " stk: ", stk, " pop: ", pop, " n: ", N)
        return not stk  # and ii >= N-1
