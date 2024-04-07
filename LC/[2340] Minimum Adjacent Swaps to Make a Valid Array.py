#############
# 20240407
#############
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        """
        * nums[ii]: 
        + 
        => min swaps to make nums valid
        # Greedy Heuristic
        - identify the min/max: O(N)
        - who is closer to the end
        1. move the closer one first
        2. move the other one after

        ----
        1. identify the left most min
        2. identify the right most max
        3. is there crossing? if yes, -1

        N=10^5
        """
        mx = max(nums)  # T:N
        mn = min(nums)  # T:N

        N = len(nums)
        for ii in range(N):
            if nums[ii] == mn:
                lmin = ii
                break
        for ii in reversed(range(N)):
            if nums[ii] == mx:
                rmax = ii
                break

        is_crossing = False
        if lmin > rmax:
            is_crossing = True

        moves = lmin + (N-rmax-1)
        if is_crossing:
            moves -= 1

        return moves


#############
# 20240114
#############
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        """
        1. find index of max
        2. move it
        3. find min
        4. just count
        """
        N = len(nums)
        mx = max(nums)
        mxi = N
        for ii in reversed(range(N)):
            if nums[ii] == mx:
                mxi = ii
                break
        mn = min(nums)
        mni = 0
        for ii, nn in enumerate(nums):
            if nn == mn:
                mni = ii
                break
        """
        0 1 2 3 4        
        1 3 5 4 2
        """
        if mxi >= mni:
            return N-mxi - 1 + mni
        else:
            return N-mxi - 1 + mni - 1


#############
# 20231007
#############
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        mxn = -math.inf
        mxi = -1
        if N == 1:
            return 0
        for ii, vv in enumerate(nums):
            mxn = max(vv, mxn)
            if mxn == vv:
                mxi = ii
        cnt = 0
        for ii in range(mxi, N-1):
            nums[ii], nums[ii+1] = nums[ii+1], nums[ii]
            cnt += 1

        mnn = math.inf
        mni = 0
        for ii, vv in enumerate(nums):
            if vv < mnn:
                mnn = vv
                mni = ii

        return cnt+mni

###############################


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)

        N = len(nums)
        rr = N-1
        while rr >= 0 and nums[rr] != mx:
            rr -= 1

        cnt = 0
        while rr+1 < N:
            cnt += 1
            nums[rr], nums[rr+1] = nums[rr+1], nums[rr]
            rr += 1

        ll = 0
        while ll < N and nums[ll] != mn:
            ll += 1

        cnt += ll

        return cnt
