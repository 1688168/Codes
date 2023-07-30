from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Count element
        v2cnt = Counter(nums)

        mxf=-1
        mxv=-1
        for vv, ff in v2cnt.items():
            if ff > mxf:
                mxf=ff
                mxv=vv
        
        # check if split is possible or not
        count=0
        for ii in range(len(nums)):
            if nums[ii]==mxv:
                count+=1
            if count *2 > (ii+1) and (mxf - count)*2 > (len(nums) - ii - 1): return ii
        
        return -1

###########
# 20230730: this binary search attempt failed
###########


from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        * Binary Search
        * find a mid-point:
          if left and right have same dominant-> move left
          if right dominant freq > left -> move right
          else:
             move left
        """

        #print("==================")
        N=len(nums)
        ll, rr = 0, len(nums)-1
        ans=-1


        def get_dom_freq(arr):
            v2cnt=Counter(arr)

            mxf=-1
            mxv=-1
            N=len(arr)
            for vv, ff in v2cnt.items():
                if ff > mxf:
                    mxf=ff
                    mxv=vv
            
            if mxf*2 > N:
                return (mxv, mxf)
            else:
                return (None, None)

        def is_left_has_right(idx):
            right=set(nums[idx:])
            for n in nums[:idx]:
                if n in right: return True
            return False


        while ll <= rr:
            mm=ll+(rr-ll)//2
            print(" mm: ", mm)
            left_dom, left_freq = get_dom_freq(nums[:mm+1])
            right_dom, right_freq = get_dom_freq(nums[mm+1:])
            print("(ld, lf): ", left_dom, left_freq)
            print("(rd, rf): ", right_dom, right_freq)
            if left_dom is not None and right_dom is not None and left_dom==right_dom:
                ans=mm
                rr=mm-1
            elif is_left_has_right(mm):
                rr=mm-1
            else:
                ll=mm+1

        
        return ans
