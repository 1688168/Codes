############
# 20230820
############

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        sum(A-B) = sum(a)-sum(b)
        """

        N=len(nums)
        prev_smaller=[-1]*N
        next_smaller=[N]*N
        prev_greater=[-1]*N
        next_greater=[N]*N

        # precalc next smaller
        stk=[]
        for ii in range(N):
            while len(stk) > 0 and nums[ii] < nums[stk[-1]]:
                next_smaller[stk[-1]]=ii
                stk.pop()
            stk.append(ii)
        
        # precalc prev smaller
        stk=[]
        for ii in reversed(range(N)):
            while len(stk) > 0 and nums[ii] <= nums[stk[-1]]:
                prev_smaller[stk[-1]]=ii
                stk.pop()
            stk.append(ii)


        # precalc next greater
        stk=[]
        for ii in range(N):
            while len(stk) > 0 and nums[ii] > nums[stk[-1]]:
                next_greater[stk[-1]]=ii
                stk.pop()
            stk.append(ii)
        
        # precalc prev greater
        stk=[]
        for ii in reversed(range(N)):
            while len(stk) > 0 and nums[ii] >= nums[stk[-1]]:
                prev_greater[stk[-1]]=ii
                stk.pop()
            stk.append(ii)
        
        res=0
        # calc result
        mx_sum=0
        mn_sum=0

        """
        0 1 2 3 4 5
            ^
        """

        for ii, vv in enumerate(nums):
            ll=ii-prev_greater[ii]
            rr=next_greater[ii]-ii
            mx_sum += vv*ll*rr

            ll=ii-prev_smaller[ii]
            rr=next_smaller[ii]-ii
            mn_sum += vv*ll*rr

        return mx_sum-mn_sum




#######################################################################
"""
: Objectives: sum(subarray_max-subarray_min)
              = sum(subarray_max)-sum(subarray_min)
: consider sum(subarray_min)
   0 1 2 3 4  5 6 7 8 9
  -1 x x x x ii x x x N
   a                  b
   make ii the max of subarrays
   ii contributes to subarrays btn [a+1~ii), [ii~b-1)
   ii contributes (ii-a)*(b-ii)*nums[ii]


 : solution:
 : 1. precalc prev_smaller, next smaller or equal
 : 2. precalc prev_larger, next larger or equal
 : 3. for each ii:
"""


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        """
        : sum(subarray_max-subarray_min)
        : = sum(subarray_max)-sum(subarray_min)
        1. for each ii, find prev/next smaller/greaterOrEqual
        2. for each ii sum max - A
        3. for each ii sum min - B
        4. return A-B
        """

        # find prev/next smaller for each ii
        N=len(nums)

        prev_smaller=[-1]*N
        next_smaller_or_equal=[N]*N

        stack=[]
        for ii in range(N):
            while len(stack)>0 and nums[ii] <= nums[stack[-1]]:
                next_smaller_or_equal[stack[-1]]=ii
                stack.pop()
            if len(stack) > 0: prev_smaller[ii]=stack[-1]
            stack.append(ii)

        # print("prev_smaller: ", prev_smaller)
        # print("next_smaller_or_equal: ", next_smaller_or_equal)

        prev_bigger=[-1]*N
        next_bigger_or_equal=[N]*N

        stack=[]
        for ii in reversed(range(N)):
            while len(stack) > 0 and nums[ii]>nums[stack[-1]]:
                prev_bigger[stack[-1]]=ii
                stack.pop()

            if len(stack) > 0: next_bigger_or_equal[ii]=stack[-1]
            stack.append(ii)

        # print("prev_bigger: ", prev_bigger)
        # print("next_bigger_or_equal: ", next_bigger_or_equal)

        res=0
        for ii in range(N):
            res += nums[ii]*(ii-prev_bigger[ii])*(next_bigger_or_equal[ii]-ii)
            res -= nums[ii]*(ii-prev_smaller[ii])*(next_smaller_or_equal[ii]-ii)

        return res


        
