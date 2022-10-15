from collections import defaultdict
class Solution:
    def largestVariance(self, s: str) -> int:
        """
        : we cannot bruteforce all subarrays -> O(N^2)
        : Variance -> need two chars
        : -> find all pairs of existing chars. 26^26
        : -> convert the string to 1, 0 , -1 array
        : -> Kadane's algorithm to find max subarray sum -> O(N)
        : -> O(26^2*N)

        : ----
        : instead of constructing the full 1, 0, -1 array, why not just visiting those index on (a, b) pair?
        : * pre-collect indexes of all chars
        """


        # find all chars
        charset=set(list(s))
        N=len(s)

        # collect char index lookup
        # char2idx = defaultdict(list)
        # for ii, c in enumerate(s):
        #     char2idx[c].append(ii)


        # try all pairs of existing chars
        ans=0
        for a in charset: #for each pair, we only visit their indexes
            for b in charset:
                if a==b: continue # ignore if a==b

                dp1=0             # max subarray sum ending with idx ii and contains no -1
                dp2=float('-inf')/2 # max subarray sum ending with idx ii and contains -1

                for ii in range(N):
                    if s[ii]==a:
                        dp1 += 1
                        dp2 += 1
                    elif s[ii]==b:
                        dp2=max(dp1-1, dp2-1)
                        dp1=0

                    ans=max(ans, dp2)

        return ans
        
