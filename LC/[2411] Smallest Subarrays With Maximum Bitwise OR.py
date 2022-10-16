class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """

        """
        bit_cnt=[0]*32

        N=len(nums)
        res=[0]*N

        jj=N-1

        def is_ok_to_remove(nn, bit_cnt):
            for ii in range(32):
                if bit_cnt[ii] > 0 and bit_cnt[ii] - (nn>>ii & 1) <= 0: return False
            return True


        for ii in reversed(range(N)):
            #accumulate bits from (N-1)~ii
            for kk in range(32):
                bit_cnt[kk] += ((nums[ii] >> kk) & 1)

            while jj > ii and is_ok_to_remove(nums[jj], bit_cnt):
                for kk in range(32):
                    bit_cnt[kk] -= ((nums[jj]>>kk) & 1)
                jj -= 1

            res[ii]=jj-ii+1

        return res
