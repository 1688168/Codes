

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
