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
            we are pairing two sorted array - two pointer: o(n)
            ### n1*n2 <= mm

            1. mm >=0
              a. n1 > 0: n2 <= mm/n1 => upper bound decreasing when n1 increasing
              b. n1==0 : all nums2
              c. n1 < 0: n2 >= mm/n1 => lower bound decreasing when n1 increasing (negative number increasing is getting smaller)
            2. mm < 0
              a. n1 > 0: n2 <= mm/n1 => upper bound increasing when n1 increasing (mm is negative)
              b. n1 == 0: since mm < 0 -> nothing added
              c. n1 < 0: n2 >= mm/n1 => lower bound increasing when n1 increasing (n1 is negative)
            """
            cnt = 0
            if mm >= 0:
                jj1 = len(nums2)-1
                jj2 = len(nums2)-1
                for ii, n1 in enumerate(nums1):  # mm > 0, n1 > 0 => n2 > 0.
                    if n1 > 0:  # n2 <= mm/n1
                        while jj1 >= 0 and n1*nums2[jj1] > mm:
                            jj1 -= 1
                        cnt += (jj1+1)

                    elif n1 == 0:
                        cnt += len(nums2)
                    else:  # n1 < 0 => n2 >= mm/n1
                        """
                        - mm > 0
                        - n1 < 0
                        - n2 < 0
                        ==> n1*n2 <=mm
                        => (negative) n1 increasing (approaching zero)
                        => (negative) n2 decreasing (6/-3=-2, 6/-2=-3, ...)


                        mm=6
                        n1: -3, -2, -1
                        mm/n1: -2, -3, -6
                        """
                        while jj2 >= 0 and n1*nums2[jj2] <= mm:
                            jj2 -= 1
                        """
                        0 1 2 3 4 (len=5)
                          ^
                        2, 3, 4 are valid => 5-1-1
                        """
                        cnt += len(nums2)-(jj2+1)

            else:  # mm < 0
                jj1 = 0
                jj2 = 0
                for ii, n1 in enumerate(nums1):  # mm > 0, n1 > 0 => n2 > 0.
                    if n1 > 0:  # n2 <= mm/n1, n2 is negative, the bigger the n1, the bigger the n2
                        while jj1 < len(nums2) and n1*nums2[jj1] <= mm:
                            jj1 += 1
                        cnt += jj1

                    elif n1 == 0:
                        cnt += 0
                    else:  # n1 < 0 and mm < 0 => n2 > 0 => the bigger the n1, the smaller the n2
                        """
                        n1*n2 <= mm
                        mm = -6
                        n1 = -3, -2, -1
                        n2 = 2    3   6
                        """
                        while jj2 < len(nums2) and n1*nums2[jj2] > mm:
                            jj2 += 1

                        cnt += len(nums2)-(jj2)

            return cnt

        ll, rr = -int(1e10), int(1e10)
        ans = ll

        while ll <= rr:
            mm = ll+(rr-ll)//2
            # print(" ll: ", ll, " rr: ", rr, " mm: ", mm)
            if count(mm) < k:
                ll = mm+1
            else:
                ans = mm
                rr = mm-1

        return ans
