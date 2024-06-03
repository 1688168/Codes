################
# 20240602
################
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        # I/O: 
        + books[ii]: [thickness_i, height_i]
        + shelfWidth: range you can go back
        => min ttl height
        # Analysis:
        + N=1000
        """
        N=len(books)

        # declare the dp
        dp=[math.inf]*N # dp[ii]: min ttl height of bookshelf ending with iith book

        # initialize DP
        dp[0]=books[0][1]

        for ii in range(1, N):
            mx=0
            cth=0
            ch=0
            for jj in reversed(range(ii+1)):
                cth+=books[jj][0]
                ch=books[jj][1]
                mx=max(mx, ch)
                if cth > shelfWidth: break #exceed shelf width
                dp[ii] = min(dp[ii], (dp[jj-1] if jj-1 >= 0 else 0)+mx)

        return dp[-1]
################
# 20240511
################
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        # single array: look-back for jj with range
        """
        books=[[0,0]]+books # insert dummy head whenever we are looking back for jj
        N=len(books)

         # initialize the DP
        dp=[math.inf]*N
        dp[0]=0

        for ii in range(1, N):#ii is the last book. how many jj we can fit in curr shelf ending @ ii?
            tt, hh = books[ii] # unpack books[ii] as the last book on current shelf
            curr_max_height=hh
            curr_width=tt
            dp[ii]=hh+dp[ii-1]
            for jj in reversed(range(1, ii)): #how many more books we can also place on same shelf with ii? (try jj backward)
                jt, jh = books[jj] #unpack jj
                if jt+curr_width > shelfWidth: break
             
                curr_width+=jt
                curr_max_height=max(curr_max_height, jh)
                dp[ii]=min(dp[ii], dp[jj-1]+curr_max_height) #the dp[jj-1] here uses the dp[0]
            
        return dp[-1]
                
        

########################
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """
        minimize the maximum of all the subarrays
        dp[ii]: the min possible height for books upto ii

        * if you know the min height of each jj before ii.
        -> min height ending @ ii is
        1. try each jj prior to ii @ same level until the current level could not fit
        2. jj-1 is the prev level and we know dp[jj] is the min hight @ jj
        """
        books = [[0, 0]]+books
        N = len(books)
        dp = [math.inf]*N
        dp[0] = 0  # height of zero books is zero
        for ii in range(1, N):
            max_height = 0  # current level height
            ttl_width = 0
            # for each ii as the last book on this level
            # jj is the first book of this level, jj could be ii
            for jj in reversed(range(1, ii+1)):
                # find the max height of current level
                max_height = max(max_height, books[jj][1])
                ttl_width += books[jj][0]
                if ttl_width > shelfWidth:
                    break
                dp[ii] = min(dp[ii], dp[jj-1]+max_height)

        return dp[-1]
