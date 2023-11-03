class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        """
        ttl_beauty=A+B
        A=num_complete_gardens*full
        B=min_num_of_flowers_incomplete*partial(0 if no incomplete)

        max(ttl_beauty)

        ===
        maximize: complete_garden_numbers * full + smallest_value_in_incomplete_gardens*partial

        - (presum[:p]+new_flowers)/(p+1) >= nums[p]
        => nums[p]*(p+1) <= presum[:p]+new_flowers

        define diff[p] as number of new_flowers we need to make all gardends up to p = nums[p]

        diff[p] <= New_Flower
        """
        flowers.sort()

        # remove completed so we can focus on those we need to fill
        ret0 = 0
        while len(flowers) > 0 and flowers[-1] >= target:
            ret0 += full
            flowers.pop()

        if len(flowers) == 0:
            return ret0  # all gardens are complete

        N = len(flowers)  # the remaining flowers length

        presum = [0]*N
        diff = [0]*N
        for ii in range(N):
            presum[ii] = (presum[ii-1] if ii > 0 else 0) + flowers[ii]
        for ii in range(N):
            diff[ii] = (ii+1)*flowers[ii]-presum[ii]
        # try all the ii where all index > ii be filled to complete
        ret = 0
        for ii in reversed(range(N)):
            if newFlowers < 0:
                break
            """
              we agreed 0~ii are incomplete, we cannot fill them >= target, cuz  eventually those will be applied with partial, 
              if we make them reach target, then the calculation will be wrong unless we apply full (the correct factor)
            """
            # here at most we can reach target-1
            # per above, we cannot have idx <= ii greater or equal to target
            if presum[ii]+newFlowers >= (ii+1)*(target-1):
                # from ii+1~N-1 inclusive is N-1 - (ii-1)+1=N-ii-1+1+1=N-1-ii
                ret = max(ret, (target-1)*partial + (N-1-ii)*full)
            else:  # binary search a p to make 0~p (inclusive) equal
                # be careful on the range of diff we do binary search
                # from 0~ii find a p that we can make equal
                idx = bisect.bisect_right(diff[:ii+1], newFlowers)
                idx -= 1  # move forward one step (study bisect_right)
                ttl = presum[idx]+newFlowers
                each = ttl//(idx+1)
                ret = max(ret, each*partial+(N-1-ii)*full)

            # by moving ii to the left, indicating we fill flowers[ii] to target. and rest for 0~(ii-1)
            newFlowers -= (target-flowers[ii])

        if newFlowers >= 0:  # we can fill all > target
            ret = max(ret, N*full)  # consider this extra case.
        return ret+ret0
