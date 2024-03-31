##########
# 20240331
##########

class Solution:
    def largestVariance(self, s: str) -> int:
        char2idx = collections.defaultdict(list)
        for ii, cc in enumerate(s):
            char2idx[cc].append(ii)

        # max subarray sum with both (a, b) -> modified Kadane (DP) -> N

        mxv = 0
        # for each pair (aa, bb), this determined an array where aa=1, bb=-1 others=0
        for aa, aii in char2idx.items():  # T: 26
            for bb, bii in char2idx.items():  # T: 26
                if aa == bb:
                    continue  # already default mxv=0
                # here we will perform the modifed Kadane
                dp_no_b = 0
                dp_has_b = -math.inf
                ii, jj, kk = 0, 0, 0  # this is index into aii, bii, not index into s

                # traversing the array on aii and bii only (cuz all others are zero and not relevent)
                while ii < len(aii) or jj < len(bii):
                    tmp_no_b = dp_no_b
                    tmp_has_b = dp_has_b

                    if ii < len(aii) and jj < len(bii):
                        if aii[ii] <= bii[jj]:
                            kk = aii[ii]
                            ii += 1
                        else:
                            kk = bii[jj]
                            jj += 1
                    elif ii < len(aii):
                        kk = aii[ii]
                        ii += 1
                    elif jj < len(bii):
                        kk = bii[jj]
                        jj += 1

                    else:
                        break

                    if s[kk] == aa:  # it's an a with value 1
                        dp_no_b = tmp_no_b + 1
                        dp_has_b = tmp_has_b + 1
                    else:
                        dp_no_b = 0
                        dp_has_b = max(tmp_no_b, tmp_has_b)-1

                    mxv = max(mxv, dp_has_b)

        return mxv


##########
# 20240331
##########
class Solution:
    def largestVariance(self, s: str) -> int:
        """
        => diff of two char frequency
        -> let two chars be (a, b)
        -> a, b = 1, -1, and others be 0
        -> variance of (a, b) =. sum(subarray)
        -> max subarray sum with both (a, b) -> modified kadane
        -> all subarray and calc all paris -> 26*26*N^2
        -> all pairs and modfied kadane
        -> 26*26*N
        """
        # get all char and it's locations
        # for each pair-> jumping from left to right on locations of the pair and apply modified_Kadane

        # get char and location

        char2idx = collections.defaultdict(list)

        for ii, cc in enumerate(s):
            char2idx[cc].append(ii)
        if len(char2idx) < 2:
            return 0

        mxv = 0  # max var can only be >= 0
        # for each pair, apply modified Kadane
        for aa, aii in char2idx.items():  # select an a (T:26)
            for bb, bii in char2idx.items():  # select a b (T:26)
                if aa == bb:
                    continue  # if aa==bb -> mxv=0 -> already default to zero

                # calc max subarray sum (modified kadane)
                dp_no_b = 0  # Max subarray sum -> Kadane -> must has two elements -> modified Kadane
                dp_has_b = -int(1e4)
                na, nb = len(aii), len(bii)
                ii, jj, kk = 0, 0, 0

                # Modified Kadane for elements in aii, bii
                # Modified Kadane on selected index (aii, bii)
                while ii < na or jj < nb:
                    tmp_no_b = dp_no_b
                    tmp_has_b = dp_has_b

                    # max subarray sum ending @ kk (kk can only be from aii, bii)
                    # hopping on a or b's locations only (for each elements)
                    if ii < na and jj < nb:  # identify the start of the subarray.  whoever has smaller index is the start of the subarray
                        if aii[ii] <= bii[jj]:
                            kk = aii[ii]
                            ii += 1
                        else:
                            kk = bii[jj]
                            jj += 1
                    elif ii < na:
                        kk = aii[ii]
                        ii += 1
                    elif jj < nb:
                        kk = bii[jj]
                        jj += 1
                    else:
                        break

                    # kk is the ending elements for modified-kadane to calc max subarray sum ending @ kk
                    if s[kk] == aa:
                        dp_has_b = tmp_has_b + 1
                        dp_no_b = tmp_no_b + 1
                    else:
                        dp_has_b = max(tmp_has_b - 1, tmp_no_b - 1)
                        dp_no_b = 0

                    mxv = max(mxv, dp_has_b)

        return mxv


##########
# 20240302
##########
class Solution:
    def largestVariance(self, s: str) -> int:
        """
        => diff of two char frequency
        -> let two chars be (a, b)
        -> a, b = 1, -1, and others be 0
        -> variance of (a, b) =. sum(subarray)
        -> max subarray sum with both (a, b) -> modified kadane
        -> all subarray and calc all paris -> 26*26*N^2
        -> all pairs and modfied kadane
        -> 26*26*N
        """
        # get all char and it's locations
        # for each pair-> jumping from left to right on locations of the pair and apply modified_Kadane

        # get char and location

        char2idx = collections.defaultdict(list)

        for ii, cc in enumerate(s):
            char2idx[cc].append(ii)
        if len(char2idx) < 2:
            return 0

        mxv = -int(1e5)
        # for each pari, apply modified Kadane
        for aa, aii in char2idx.items():
            for bb, bii in char2idx.items():
                if aa == bb:
                    continue

                dp_no_b = 0
                dp_has_b = -int(1e4)
                na, nb = len(aii), len(bii)
                ii, jj, kk = 0, 0, 0
                while ii < na or jj < nb:
                    tmp_no_b = dp_no_b
                    tmp_has_b = dp_has_b

                    # hopping on a or b's locations only
                    if ii < na and jj < nb:
                        if aii[ii] <= bii[jj]:
                            kk = aii[ii]
                            ii += 1
                        else:
                            kk = bii[jj]
                            jj += 1
                    elif ii < na:
                        kk = aii[ii]
                        ii += 1
                    elif jj < nb:
                        kk = bii[jj]
                        jj += 1
                    else:
                        break

                    if s[kk] == aa:
                        dp_has_b = tmp_has_b + 1
                        dp_no_b = tmp_no_b + 1
                    else:
                        dp_has_b = max(tmp_has_b - 1, tmp_no_b - 1)
                        dp_no_b = 0

                    mxv = max(mxv, dp_has_b)

        return mxv

###############


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
