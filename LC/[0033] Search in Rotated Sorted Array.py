class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

                  7
              6
           5
        4

                           2
                        1
                     0


        """


        N=len(nums)
        ll, rr = 0, N-1
        ans=-1
        while ll <= rr:
            mm=ll+(rr-ll)//2
            curr=nums[mm]

            if curr==target: #found it
                return mm

            if curr < nums[0]: #landed on the right
                if target < curr or target > nums[N-1]:
                    rr=mm-1
                else:
                    ll=mm+1

            else: # landed on the left
                if curr < target or target < nums[0]:
                    ll=mm+1
                else:
                    rr=mm-1


        return ans

########################################################
########################################################

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ll, rr, ans = 0, len(nums)-1, -1


        while ll <= rr:
            mm=ll+(rr-ll)//2

            if nums[mm]==target:
                return mm

            if nums[mm] >= nums[0]: # on the left

                if nums[mm] < target or target < nums[0]:
                    ll=mm+1
                else:
                    rr=mm-1


            else: # on the right

                if target < nums[mm] or target >= nums[0]:
                    rr=mm-1
                else:
                    ll=mm+1

        return ans
