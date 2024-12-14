class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N=len(nums)

        ll=min(nums)
        rr=sum(nums)
        ans=0

        def isFeasible(mm):
            """
            * how many partitions do you need to fit in all subarrays with sum less than or equal to mm
            """
            ttl=0
            cnt=0

            ii=0
            while ii<N:
                #print("ii: ", ii, " mm: ", mm)
                jj=ii

                while jj<N and nums[jj]+ttl <= mm:
                    ttl+=nums[jj]
                    jj+=1
                
                cnt+=1
                if cnt > k: return False
                ttl=0
                ii=jj
                    
            return cnt <= k

        while ll<=rr:
            mm=ll+(rr-ll)//2

            if(isFeasible(mm)):
                ans=mm
                rr=mm-1
            else:
                ll=mm+1
        
        return ans



    

        