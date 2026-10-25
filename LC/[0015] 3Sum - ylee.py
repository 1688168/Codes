class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Return unique triplets that sum to zero."""
        nums.sort()

        def twoSum(idx, target):
            ll, rr = idx + 1, len(nums) - 1
            res = []

            while ll < rr:
                aa = nums[ll]
                bb = nums[rr]

                if aa + bb == target:
                    res.append([aa, bb])
                    ll += 1
                    rr -= 1
                elif aa + bb > target:
                    rr -= 1
                else:
                    ll += 1

                # Skip previously considered values to avoid duplicate pairs.
                while rr < len(nums) - 1 and rr > ll and nums[rr] == nums[rr + 1]:
                    rr -= 1
                while ll > idx + 1 and ll < rr and nums[ll] == nums[ll - 1]:
                    ll += 1

            return res

        res = []
        for ii, nn in enumerate(nums[:-2]):
            # Reusing a fixed value would produce the same triplets.
            if ii > 0 and nums[ii] == nums[ii - 1]:
                continue

            pairs = twoSum(ii, -nn)
            for pair in pairs:
                res.append(pair + [nn])

        return res