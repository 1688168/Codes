class Solution:

    def maxSumMinProduct(self, nums: List[int]) -> int:
        """
        : a x x x x ii x x x b
        * 1. find prev-smaller
                  next-smaller
        * 2. calc presume
        * 3. traverse the array calc min-product
        * 4. capture the max
        * 5. return the max
        """
        M=pow(10, 9)+7
        N=len(nums)
        presum=[0]*N

        for ii in range(N):
            if ii == 0:
                presum[ii]=nums[ii]
            else:
                presum[ii]=presum[ii-1]+nums[ii]

        prev_smaller=[-1]*N
        next_smaller=[N]*N

        stack=[]
        for ii, vv in enumerate(nums):
            while len(stack) > 0 and vv < nums[stack[-1]]:
                next_smaller[stack[-1]]=ii
                stack.pop()

            if len(stack) > 0:
                prev_smaller[ii]=stack[-1]
            stack.append(ii)

        mxv=0
        # print("presum: ", presum)
        # print("prev_smaller: ", prev_smaller)
        # print("next_smaller: ", next_smaller)
        # print(" M: ", M)
        for ii in range(N):
            prev= prev_smaller[ii]
            nxt = next_smaller[ii]
            a=presum[prev] if prev != -1 else 0
            b=presum[nxt-1]
            mprod= ((b-a) * nums[ii])

            mxv=max(mxv, mprod)

        return mxv%M
