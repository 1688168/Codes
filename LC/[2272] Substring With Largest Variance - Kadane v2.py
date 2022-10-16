class Solution:
    def largestVariance(self, s: str) -> int:
        """
        : we cannot bruteforce all subarrays -> O(N^2)
        : Variance -> need two chars
        : -> find all pairs of existing chars. 26^26
        : -> convert the string to 1, 0 , -1 array
        : -> Kadane's algorithm to find max subarray sum -> O(N)
        : -> O(26^2*N)
        """

        # find all chars
        charset=set(list(s))
        N=len(s)
        # try all pairs of existing chars
        res=0
        for a in charset:
            for b in charset:
                if a==b: continue # ignore if a==b

                # we need both a, and one b in the subarray.
                # for each b we found, we do left Kadane and right Kadane
                arr = [0]*N
                for ii in range(N):
                    if s[ii]==a:
                        arr[ii]=1
                    elif s[ii]==b:
                        arr[ii]=-1

                dp0=[0]*N

                for ii in range(N):
                    dp0[ii]= arr[ii] if ii==0 else max(dp0[ii-1]+arr[ii], arr[ii])

                lmx=float('-inf')
                for ii in reversed(range(N)):
                    dp1=arr[ii] if ii == N-1 else max(arr[ii], dp1+arr[ii])

                    if arr[ii]==-1:
                        lmx=max(lmx, dp1+dp0[ii]-arr[ii])

                res=max(res, lmx)
        return res
        
