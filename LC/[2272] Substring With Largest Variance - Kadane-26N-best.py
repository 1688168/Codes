
class Solution:
    def largestVariance(self, s: str) -> int:
        """
        variance: largest diff btn occurance of two chars
        diff of two chars -> (a,b)=(-1, 1) => sum is the diff
        the sub-array sum must contain both (a, b) => modified kadane

        kadane dp[ii] = max(nums[ii], nums[ii]+dp[ii-1])
        => largest variance of all substrings

                i
        x x x x x x x x x

        modified kadane is O(N) * 26 * 26 

        1. get all pairs
        2. get all locations of each char

        """
        char2Idx = collections.defaultdict(list)
        for ii, cc in enumerate(s):
            char2Idx[cc].append(ii)

        # we now knows all chars and it's idx

        # try all pairs
        mxv = -math.inf
        for a, a_idx in char2Idx.items():
            for b, b_idx in char2Idx.items():
                if a == b:
                    mxv = max(mxv, 0)
                    continue

                Na = len(a_idx)
                Nb = len(b_idx)
                ii, jj = 0, 0

                """
                ii=[0, 3, 9, 12]
                jj=[1, 2, 5, 15]
                """

                sum_no_b = 0
                sum_has_b = -math.inf//2

                while ii < Na or jj < Nb:

                    if jj >= Nb or (ii < Na and a_idx[ii] < b_idx[jj]):

                        sum_no_b += 1
                        sum_has_b += 1
                        ii += 1

                    elif ii >= Na or (jj < Nb and b_idx[jj] < a_idx[ii]):

                        sum_has_b = max(sum_no_b-1, sum_has_b-1)
                        # sum_has_b = max(sum_has_b-1, sum_no_b-1) #I actually do not understand why this line is diff than prev line
                        sum_no_b = 0
                        jj += 1

                    mxv = max(mxv, sum_has_b)

        return mxv
