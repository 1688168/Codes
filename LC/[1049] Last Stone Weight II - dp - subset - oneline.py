class Solution:
    def lastStoneWeightII(self, A):
        # for each stone, 
        """
        * {0} is the initial value for dp, indicating 0 is achievable by doing nothing
        * A is the list to be reduced
        * for each stone, we keep union (x+y) set and abs(x-y) set
        """
        return min(reduce(lambda dp, y: {x + y for x in dp} | {abs(x - y) for x in dp}, A, {0}))
        