class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        """
        -. sort nums

        0 1 2 3 4 5 6
        x y z w o o o
            ii

        ii=3
        power_of_heros[ii] = nums[ii]* nums[ii]^2
                        | z * 2^0 * nums[ii]^2 | ===> Prev
                        | y * 2^1 * nums[ii]^2 |
                        | x * 2^2 * nums[ii]^2 |

        ii=4
        power_of_heros[ii] = nums[ii]* nums[ii]^2
                            w * 2^0 * nums[ii]^2
                        |   z * 2^1 * nums[ii]^2 |===> prev*2
                        |   y * 2^2 * nums[ii]^2 |
                        |   x * 2^3 * nums[ii]^2 | 

        power_of_heros[ii] = (prev*2+nums[ii-1]) * nums[ii]^2 + nums[ii] * nums[ii]^2 

        ii  prev    power_of_heros[ii]
        0   0       0                          +  nums[0]*nums[0]^2
                    ^^^^                    
                    prev

        1           prev=prev*2+nums[ii-1]
            x       (prev)*nums[ii]^2           +  nums[ii]*nums[ii]^2
        ....
        """
        nums.sort()
        M = int(1e9+7)
        N = len(nums)
        prev = 0
        ttl = 0
        for ii, vv in enumerate(nums):
            square = pow(nums[ii], 2) % M
            if ii >= 1:
                prev = ((prev*2) % M+nums[ii-1]) % M
            ttl += ((prev) * square + square*nums[ii]) % M
            ttl %= M
        return ttl
