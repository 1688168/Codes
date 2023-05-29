############
## 20230528
############
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        def twoSum(curr, nums, target, res):
            ll, rr = 0, len(nums)-1
            while ll < rr:
                if nums[ll]+nums[rr] == target:
                    res.append((curr, nums[ll], nums[rr]))
                    ll+=1
                    while ll < rr and nums[ll]==nums[ll-1]:
                        ll+=1                                                    
                else:
                    if nums[ll]+nums[rr] > target:
                        rr-=1
                    else:
                        ll+=1
           
        for ii, nn in enumerate(nums[:-2]):
            if ii > 0 and nn==nums[ii-1]: continue
            ntarget=0-nn
            twoSum(nn, nums[ii+1:], ntarget, res)


        return res


#######
# 20230122
#######
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort in place increasing order
        N=len(nums)
        res=[]
        ii=0
        while ii < N-2:
            ll, rr = ii+1, N-1
            a=nums[ii]
            while ll < rr:
                b, c = nums[ll], nums[rr]
                if a+b+c > 0:
                    rr -=1
                elif a+b+c < 0:
                    ll+=1
                else:
                    res.append((a, b, c))
                    ll+=1
                    while ll < N-1 and ll > 0 and nums[ll]==nums[ll-1]:
                        ll+=1
            ii+=1
            while ii >0 and ii < N-2 and nums[ii]==nums[ii-1]:
                ii+=1


        return res

#####################################################
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
