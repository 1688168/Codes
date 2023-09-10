        """
        => sum(min*sub_sum)
        a x x x x ii x x x b
          1 2 3 4    3 2 1      
        
        ttl = (left * (b-ii) + nums[ii] * (b-ii) * (ii-a) + right*(ii-a)) * nums[ii]
        left = nums[a+1]*1 + nums[a+2]*2 + nums[a+3]*3 + nums[a+4]*4
        let presum2 = nums[1]*1 + nums[2]*2 + ...

        presum2[ii]-presum2[a] = nums[a+1]*(a+1)+nums[a+2]*(a+2) + ...
                               = presum[a+1:ii] * a + left
        >>> left = presum2[ii]-presum2[a] - presum[a+1:ii]*a

        -----
        right = nums[ii+1] * 3 + nums[ii+2]*2 + nums[ii+3]*1

        presum2[b-1]-presum2[ii] = nums[ii+1] * 1 + nums[ii+2] * 2 + ...
                                 = presum[ii+1: b-1] * b - right        


        >>> right = presum[ii+1:b-1] * b - (presum2[b-1] - presum2[ii])

        nums[ii+1] * b - nums[ii+1] * 3

        -> b = ii+ 3 + 1
        -> b-3 = ii+1
        """

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        # M = pow(10, 9)+7
        M = int(1e9 + 7)
        N = len(strength)  # the original array size

        nums = [0] + strength
        presum1 = [0] * (N + 2)
        presum2 = [0] * (N + 2)

        # prepare normal/special range sum array
        for ii in range(1, N + 1):
            presum1[ii] = (presum1[ii - 1] + nums[ii]) % M
            presum2[ii] = (presum2[ii - 1] + nums[ii] * ii) % M

        # prev/next smaller
        stack = []
        next_smaller = [N + 1] * (N + 2)
        prev_smaller = [0] * (N + 2)
        for ii in range(1, N + 1):
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
        for ii in range(1, N + 1):
            a, b = prev_smaller[ii], next_smaller[ii]
            x = ii - a
            y = b - ii
            left = (presum2[ii - 1] - presum2[a]) - ((presum1[ii - 1] - presum1[a]) * a % M)
            left = left * y % M
            right = ((presum1[b - 1] - presum1[ii]) * b % M - (presum2[b - 1] - presum2[ii]))
            right = right * x % M
            mm = nums[ii] * x * y % M

            res = (res + (left + mm + right) * nums[ii]) % M

        return res

