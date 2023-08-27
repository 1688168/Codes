M = pow(10, 9)+7


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        N = len(arr)
        prev_smaller = [-1]*N
        next_smaller = [N]*N
        stk = []
        for ii, vv in enumerate(arr):
            while len(stk) > 0 and arr[stk[-1]] > vv:
                next_smaller[stk[-1]] = ii
                stk.pop()
            if len(stk) > 0:
                prev_smaller[ii] = stk[-1]

            stk.append(ii)

        for ii, vv in enumerate(arr):
            ll = prev_smaller[ii]
            rr = next_smaller[ii]
            ans += ((arr[ii]*(ii-ll)*(rr-ii)) % M)
            ans %= M

        return ans
