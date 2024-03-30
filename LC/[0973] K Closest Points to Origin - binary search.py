class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ll, rr = 0, pow(10, 9)+1
        ans=rr
        dist=[[pow(x,2)+pow(y, 2), (x, y)] for x, y in points] #N

        def count(mm):#N
            cnt=0
            for dd, (xx, yy) in dist:
                if dd <= mm:
                    cnt+=1

            return cnt


        while ll <= rr: #32
            mm=ll+(rr-ll)//2

            if count(mm) >=k:
                ans=mm
                rr=mm-1
            else:
                ll=mm+1

        return [pp for dd, pp in dist if dd <= ans]