class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        mx=2*n if n%2 != 0 else n

        ll, rr, ans = n, mx, mx

        while ll <= rr:
            mm=ll+(rr-ll)//2

            if mm%2==0 and mm%n==0:
                ans=mm
                rr=mm-1
            else:
                ll=mm+1


        return ans
