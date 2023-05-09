class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans=[0]*N
        ans1=[0]*N

        setf=set()
        setb=set()

        for ii, vv in enumerate(nums):
            if ii==0:
               
                ans[ii]=1
            else:
                if vv in setf:
                    ans[ii]=ans[ii-1]
                else:
                    ans[ii]=ans[ii-1]+1
            setf.add(vv)
         
        for ii in reversed(range(N)):
            if ii==N-1:
                ans1[ii]=0
            else:
                if nums[ii+1] not in setb:
                    ans1[ii]=ans1[ii+1]+1
                    setb.add(nums[ii+1])
                else:
                    ans1[ii]=ans1[ii+1]
        #print("ans1", ans1)

        for ii in range(N):
            ans[ii]=ans[ii]-ans1[ii]


        return ans