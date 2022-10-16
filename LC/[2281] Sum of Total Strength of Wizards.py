# As the ruler of a kingdom, you have an army of wizards at your command. 
# 
#  You are given a 0-indexed integer array strength, where strength[i] denotes 
# the strength of the iᵗʰ wizard. For a contiguous group of wizards (i.e. the 
# wizards' strengths form a subarray of strength), the total strength is defined as 
# the product of the following two values: 
# 
#  
#  The strength of the weakest wizard in the group. 
#  The total of all the individual strengths of the wizards in the group. 
#  
# 
#  Return the sum of the total strengths of all contiguous groups of wizards. 
# Since the answer may be very large, return it modulo 10⁹ + 7. 
# 
#  A subarray is a contiguous non-empty sequence of elements within an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: strength = [1,3,1,2]
# Output: 44
# Explanation: The following are all the contiguous groups of wizards:
# - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
# - [3] from [1,3,1,2] has a total strength of min([3]) * sum([3]) = 3 * 3 = 9
# - [1] from [1,3,1,2] has a total strength of min([1]) * sum([1]) = 1 * 1 = 1
# - [2] from [1,3,1,2] has a total strength of min([2]) * sum([2]) = 2 * 2 = 4
# - [1,3] from [1,3,1,2] has a total strength of min([1,3]) * sum([1,3]) = 1 * 4
#  = 4
# - [3,1] from [1,3,1,2] has a total strength of min([3,1]) * sum([3,1]) = 1 * 4
#  = 4
# - [1,2] from [1,3,1,2] has a total strength of min([1,2]) * sum([1,2]) = 1 * 3
#  = 3
# - [1,3,1] from [1,3,1,2] has a total strength of min([1,3,1]) * sum([1,3,1]) =
#  1 * 5 = 5
# - [3,1,2] from [1,3,1,2] has a total strength of min([3,1,2]) * sum([3,1,2]) =
#  1 * 6 = 6
# - [1,3,1,2] from [1,3,1,2] has a total strength of min([1,3,1,2]) * sum([1,3,1
# ,2]) = 1 * 7 = 7
# The sum of all the total strengths is 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 
# 44.
#  
# 
#  Example 2: 
# 
#  
# Input: strength = [5,4,6]
# Output: 213
# Explanation: The following are all the contiguous groups of wizards: 
# - [5] from [5,4,6] has a total strength of min([5]) * sum([5]) = 5 * 5 = 25
# - [4] from [5,4,6] has a total strength of min([4]) * sum([4]) = 4 * 4 = 16
# - [6] from [5,4,6] has a total strength of min([6]) * sum([6]) = 6 * 6 = 36
# - [5,4] from [5,4,6] has a total strength of min([5,4]) * sum([5,4]) = 4 * 9 =
#  36
# - [4,6] from [5,4,6] has a total strength of min([4,6]) * sum([4,6]) = 4 * 10 
# = 40
# - [5,4,6] from [5,4,6] has a total strength of min([5,4,6]) * sum([5,4,6]) = 4
#  * 15 = 60
# The sum of all the total strengths is 25 + 16 + 36 + 36 + 40 + 60 = 213.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strength.length <= 10⁵ 
#  1 <= strength[i] <= 10⁹ 
#  
# 
#  Related Topics Array Stack Monotonic Stack Prefix Sum 👍 645 👎 45
"""
Objective: subarray sum of strength
Def: strength: subarray-sum*weakest_value

idea: all subarrays is N^2
      all weakest points is O(N)
=> we need to findout how to calc sum of strength of subarrays on each weakest point

ex: given a subarray:
a x x x x ii x x x b
  1 2 3 4 ii 3 2 1
          5  6 7 8 9
where ii is the weakest wizard in subarray range (a, b) << not inclusive
      nums[a] is "prev smaller or equal"
      nums[b] is "next smaller or equal"  <<< use stack to find out

let left_cnt  = (ii-a): <0, 1, 2, 3, 4> num of combination of what left can be
    right_cnt = (b-ii): <0, 1, 2, 3> num of combination of what right can be

=> we are trying to figure out the ttl contribution of strength given ii is the weakest wizard
let new_presum = nums[a+1]*1 + nums[a+2]*2 + ...
    resum (regular) = nums[a+1] + nums[a+2] + ... (just a regular subarray sum)

left_strength: nums[ii] * (nums[a+1]*1 + nums[a+2]*2 + ... + nums[a+ii-1-a]*(ii-1-a)) * right_cnt
right_strength: nums[ii] * (nums[ii+1]*3 + nums[ii+2]*2 + ... + nums[b-1]*1) * left_cnt
             =  nums[ii] * [(b-ii-1)*(nums[ii+1]+num[ii+2]) + ... + nums[b-1]) - (nums[ii+1]*0 + nums[ii+2]*2 + ...)]
                                     ^^^^^^^^^^^^^^^^^^^                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                     regular presum                           new_presume
ii_strength = num[ii] * left_cnt * right_cnt

ans=left_strength+right_strength+ii_strength

=== try:
let new_presum = nums[1]*1 + nums[2]*2 + ... + nums[ii]*ii

# left:
new_presum[ii-1]-new_presum[a] = nums[a+1]*(a+1) + nums[a+2]*(a+2) + nums[a+3]*(a+3) + nums[a+4]*(a+4)
                               = "what we want" + sum[a+1: ii-1] * a

# right:
new_presum[b-1] - new_presum[ii] = nums[ii+1] * (ii+1) + nums[ii+2] * (ii+2) + nums[ii+3] * (ii+3)
                                 = b * regular_presum[ii+1: b-1] - "what we want



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

# leetcode submit region end(Prohibit modification and deletion)
