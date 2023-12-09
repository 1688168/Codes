###############
# 20231209
###############
class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        - this is looking for O(N)
        -> optimization: DP, BinarySearch, Greedy
        -> greedy
        """
        """
        rule1: 
        rule2:
        """
        N = len(ratings)
        candies = [1]*N

        # from left to rigth - rule2
        for ii in range(1, N):  # greedy always pick the local optimal solution
            if ratings[ii] > ratings[ii-1]:
                candies[ii] = candies[ii-1]+1

        # from right to left - rule2
        for ii in reversed(range(N-1)):  # always pick the local optimal solution
            if ratings[ii] > ratings[ii+1]:
                candies[ii] = max(candies[ii], candies[ii+1]+1)

        # can the result reverse in future selection
        """
        ii     : 0 1 2
        ratings: 1 0 2
        candies: 1 1 1
        from L : 1 1 1
        from R : 2 1 2
        when we do right-to-left increment, (when ii=0), we increment ii=0 will not revese previous status (left-to-right). ie, when ii=0 already enforced greater then (ii-1), making it even bigger does not reverse the existing > status
        """

        return sum(candies)


###########################
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        left_only = [1]*N
        right_only = [1]*N
        required = [0]*N

        for ii in range(1, N):
            if ratings[ii] > ratings[ii-1]:
                left_only[ii] = left_only[ii-1]+1
            if ratings[N-1-ii] > ratings[N-ii]:
                right_only[N-1-ii] = right_only[N-ii]+1

        # print("left: ", left_only)
        # print("right: ", right_only)

        for ii in range(N):
            required[ii] = max(left_only[ii], right_only[ii])

        return sum(required)
