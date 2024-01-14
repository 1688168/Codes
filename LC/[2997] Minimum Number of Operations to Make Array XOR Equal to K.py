class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = nums+[k]
        flips = 0

        max_num = max(nums)
        # print(" max_num: ", max_num)
        ii = 0
        while max_num > 0:
            mask = 1*int(pow(2, ii))
            # print(" mask: ", mask)
            ttl = 0
            for n in nums:
                # print(" n: ", n, " mask: ", mask, " bit: ",  (mask&n)//int(pow(2, ii)))
                ttl += (mask & n)//int(pow(2, ii))
            # print(" ttl: ", ttl)
            if ttl % 2 == 1:
                flips += 1
            max_num //= 2
            ii += 1

        return flips
