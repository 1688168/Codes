
#################
# 20240401
#################
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        """
        * strength[ii]: strength of iith's wizard
        * total strength of a "subarray": 
          - weakest 
          - sum(strength in the subarray)
        => sum(total_strength)
        -------------
        - analysis
        -------------
        * N=10^5
        # bruteforce
        * all subarray: N^2
        * find weakest: N 
        * subarray sum: presum look up: 1
        -> N^3
        """
        # M = pow(10, 9)+7 # pow returns int
        M = int(1e9) + 7
        nums = [0] + strength  # insert dummy in the front for presum
        N = len(nums)  # the original array size

        presum1 = [0] * N
        presum2 = [0] * N

        # prepare normal/special range sum array
        for ii in range(1, N):
            presum1[ii] = (presum1[ii - 1] + nums[ii]) % M
            presum2[ii] = (presum2[ii - 1] + nums[ii] * ii) % M

        # for min in a subarray: find prev/next smaller
        # prev/next smaller
        stack = []  # monotonic stack
        next_smaller = [N] * (N)
        prev_smaller = [0] * (N)
        for ii in range(1, N):  # 0 is a dummy
            while len(stack) > 0 and nums[ii] < nums[stack[-1]]:
                next_smaller[stack[-1]] = ii
                stack.pop()

            if len(stack) > 0:
                prev_smaller[ii] = stack[-1]
            stack.append(ii)

        # traverse along the nums (ii is the weakest) and calc the ttl strength
        res = 0
        # print("presum1: ", presum1)
        # print("presum2: ", presum2)
        # print("presmaller:", prev_smaller)
        # print("nextsmaller: ", next_smaller)
        for ii in range(1, N):  # zero is a dummy
            a, b = prev_smaller[ii], next_smaller[ii]
            x = ii - a
            y = b - ii
            left = (presum2[ii - 1] - presum2[a]) - \
                ((presum1[ii - 1] - presum1[a]) * a % M)
            left = left * y % M
            right = ((presum1[b - 1] - presum1[ii]) * b %
                     M - (presum2[b - 1] - presum2[ii]))
            right = right * x % M
            mm = nums[ii] * x * y % M

            res = (res + (left + mm + right) * nums[ii]) % M

        return res


###############################################################
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # M = pow(10, 9)+7
        M = int(1e9 + 7)
        nums = [0] + strength
        N = len(nums)  # the original array size

        presum1 = [0] * N
        presum2 = [0] * N

        # prepare normal/special range sum array
        for ii in range(1, N):
            presum1[ii] = (presum1[ii - 1] + nums[ii]) % M
            presum2[ii] = (presum2[ii - 1] + nums[ii] * ii) % M

        # prev/next smaller
        stack = []
        next_smaller = [N] * (N)
        prev_smaller = [0] * (N)
        for ii in range(1, N):
            while len(stack) > 0 and nums[ii] < nums[stack[-1]]:
                next_smaller[stack[-1]] = ii
                stack.pop()

            if len(stack) > 0:
                prev_smaller[ii] = stack[-1]
            stack.append(ii)

        # traverse along the nums (ii is the weakest) and calc the ttl strength
        res = 0
        # print("presum1: ", presum1)
        # print("presum2: ", presum2)
        # print("presmaller:", prev_smaller)
        # print("nextsmaller: ", next_smaller)
        for ii in range(1, N):
            a, b = prev_smaller[ii], next_smaller[ii]
            x = ii - a
            y = b - ii
            left = (presum2[ii - 1] - presum2[a]) - \
                ((presum1[ii - 1] - presum1[a]) * a % M)
            left = left * y % M
            right = ((presum1[b - 1] - presum1[ii]) * b %
                     M - (presum2[b - 1] - presum2[ii]))
            right = right * x % M
            mm = nums[ii] * x * y % M

            res = (res + (left + mm + right) * nums[ii]) % M

        return res
