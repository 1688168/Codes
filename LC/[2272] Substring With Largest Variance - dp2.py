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
        char2idx = defaultdict(list)
        for ii, c in enumerate(s):
            char2idx[c].append(ii)


        # try all pairs of existing chars
        ans=0
        for a in charset: #for each pair, we only visit their indexes
            for b in charset:
                if a==b: continue # ignore if a==b

                dp1=0             # max subarray sum ending with idx ii and contains no -1
                dp2=float('-inf')/2 # max subarray sum ending with idx ii and contains -1
                ii=jj=0

                while ii < len(char2idx[a]) or jj < len(char2idx[b]):
                    if jj==len(char2idx[b]) or (ii < len(char2idx[a]) and char2idx[a][ii] < char2idx[b][jj]):
                        dp1 += 1
                        dp2 += 1
                        ii+=1
                    elif ii==len(char2idx[a]) or(jj < len(char2idx[b]) and char2idx[b][jj] < char2idx[a][ii]):
                        dp2 = max(dp1-1, dp2-1)
                        dp1=0
                        jj+=1
                    ans=max(ans, dp2)

        return ans
        
