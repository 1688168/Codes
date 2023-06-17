class Solution:
    def candy(self, ratings: List[int]) -> int:
        N=len(ratings)
        left_only=[1]*N
        right_only=[1]*N
        required=[0]*N

        for ii in range(1, N):
            if ratings[ii] > ratings[ii-1]: left_only[ii] = left_only[ii-1]+1
            if ratings[N-1-ii] > ratings[N-ii]: right_only[N-1-ii] = right_only[N-ii]+1

        # print("left: ", left_only)
        # print("right: ", right_only)
        
        for ii in range(N):
            required[ii]=max(left_only[ii], right_only[ii])
        
        return sum(required)
        
