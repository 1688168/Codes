class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if len(nums1) > len(nums2):
            return self.kthSmallestProduct(nums2, nums1, k)
        """
        nums1[ii]*nums2[jj] <= mm
        1. if nums1[ii] > 0
            nums2[jj] <= floor(mm*1.0/nums1[ii])
            ret += jj+1
        2. if nums1[ii] == 0
            if mm>=0: 
                ret+= nums2.size()
            else:
                ret += 0

        3. if nums1[ii] < 0
            nums2[jj] >= ceil(mm*1.0/nums1[ii])
            ret += (n-1)-j+1

        """
        def count(mm):
            """
            we are pairing two sorted array.
            - two pointer: o(n)
            - traverse 1 and binary search the other: NlogN (only used sorted character of array2)
            """
            cnt=0
            for ii, n1 in enumerate(nums1):
                """
                n1*n2 <=mm
                if n1 > 0:
                    n2 <= mm/n1
                    idx=bisect_right
                    ret+=idx
                elif n1==0:
                    if mm >=0:
                        ret += nums2.size()
                    else:
                        ret +=0
                else:# n1 <0
                    n2 >= mm/n1
                    idx=bisect_right
                    ret+=idx
                """
             
                # n1*n2 <=mm
                if n1 > 0:#n2<=mm/n1
             
                    n2=math.floor(mm/n1)
                    idx=bisect_right(nums2, n2)
                    cnt += idx
                elif n1==0:
                    if mm >=0:
                        cnt += len(nums2)
                else:#n1 < 0
                    """
                    -3 * -2 <= 7
                    -2 >= -2.3333
                    """
                    # n2 >= mm/n1
           
                    n2 = math.ceil(mm/n1)
                    idx=bisect_left(nums2, n2)
                    """
                    
                    0 1 2 3 4 
                    len=5
                    """
                    cnt += (len(nums2)-idx)
            return cnt

        ll, rr = -int(1e10), int(1e10)
        ans=ll

        while ll <= rr:         
            mm=ll+(rr-ll)//2
            #print(" ll: ", ll, " rr: ", rr, " mm: ", mm)
            if count(mm) < k:
                ll=mm+1
            else:
                ans=mm
                rr=mm-1
        
        return ans
        