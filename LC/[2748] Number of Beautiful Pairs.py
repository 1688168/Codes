class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        N = len(nums)
        # nums.sort()
        cnt = 0
        for ii in range(N-1):
            n1 = int(str(nums[ii])[0])

            for jj in range(ii+1, N):
                n2 = int(str(nums[jj])[-1])
                if math.gcd(n1, n2) == 1:
                    # print(n1, "=", n2)
                    cnt += 1

        return cnt
