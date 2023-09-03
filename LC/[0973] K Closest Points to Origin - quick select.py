"""
https://youtu.be/xi4QVECpmxQ

"""
# 20230903
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        p = [(pow(x, 2)+pow(y, 2), ii) for ii, (x, y) in enumerate(points)]
        def qs(st, ed, k):
            nonlocal p
            pivot = p[st+(ed-st)//2][0]

            ii, jj, kk = st, st, ed
            while jj <= kk:
                if p[jj][0] < pivot:
                    p[ii], p[jj] = p[jj], p[ii]
                    ii+=1
                    jj+=1
                elif p[jj][0] == pivot:
                    jj+=1
                else:
                    p[jj], p[kk] = p[kk], p[jj]
                    kk-=1
            
            """
            s s s s o o o o L L L 
                    i     k j
                *    
            """

            if k <= (ii-st):
                return qs(st, ii-1, k)
            elif k <= jj-st:
                return pivot
            else:
                return qs(jj, ed, k-(jj-st))

        pivot = qs(0, len(p)-1, k)
        res=[]
        for ii in range(len(p)):
            if p[ii][0] <= pivot:
                res.append(points[p[ii][1]])
            else:
                break

#############################
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        : 1. calc all distance and sort to return first k -> nlogn
        : 2. use max heap. insert N distance into max heap with k -> N*logk
        : 3. quick select -> avg(N)
        """
        res = []
        # calc all distance

        dist = []
        for ii, (x, y) in enumerate(points):
            dist.append((pow(x, 2)+pow(y, 2), ii))

        def quickselect(st, ed, k):
            pivot = dist[st + (ed-st)//2][0]

            ii, jj, kk = st, st, ed
            while jj <= kk:
                if dist[jj][0] < pivot:

                    dist[ii], dist[jj] = dist[jj], dist[ii]
                    ii += 1
                    jj += 1
                elif dist[jj][0] > pivot:
                    dist[jj], dist[kk] = dist[kk], dist[jj]
                    kk -= 1
                else:
                    jj += 1

            if (ii-st) >= k:
                return quickselect(st, ii-1, k)
            elif kk-st+1 >= k:
                return pivot
            else:
                return quickselect(jj, ed, k-(jj-st))

        kthDist = quickselect(0, len(dist)-1, k)

        for d in dist:
            if d[0] <= kthDist:
                res.append(points[d[1]])

        return res
