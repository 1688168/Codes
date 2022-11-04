class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        : to avoid duplicate, we need to sort otherwise, we need to incur additional set container to remove duplicate
        """
        nums.sort()

        #for each element, check if same as prev, if so skip. anchoring this one and find the other two sum to 0

        ii = 0
        N=len(nums)
        res=[] #output space

        while ii < N:
            curr=nums[ii]
            if curr > 0: break

            if ii==0 or curr != nums[ii-1]:
                ll, rr=ii+1, N-1
                while ll > 0 and rr >= 0 and ll<rr:
                    ttl=nums[ii]+nums[ll]+nums[rr]
                    if ttl == 0:
                        res.append([nums[ii], nums[ll], nums[rr]])
                        ll+=1
                        while ll> ii+1 and ll < rr and nums[ll]==nums[ll-1]:
                            ll+=1
                    elif ttl > 0:
                        rr-=1
                    elif ttl < 0:
                        ll+=1

            ii+=1

        return res


###################
#  older try
###################
def threeSum(self, nums: List[int]) -> List[List[int]]:
    # to remove duplicate
    nums.sort()
    res=[]
    for ii, vv in enumerate(nums):
        if nums[ii] > 0: break # the array is sorted already, we cannot have sum of two bigger
                               # number equal to a smaller postive number
        if ii==0 or vv != nums[ii-1]: # handle duplicate

            #two sum
            ll, rr = ii+1, len(nums)-1
            while ll < rr:
                ttl=nums[ii]+nums[ll]+nums[rr]
                if ttl == 0:
                    res.append((nums[ii], nums[ll], nums[rr]))
                    ll+=1
                    while ll < rr and nums[ll]==nums[ll-1]:
                        ll+=1
                elif ttl > 0:
                    rr-=1
                else:
                    ll+=1

    return res
