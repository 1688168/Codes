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
