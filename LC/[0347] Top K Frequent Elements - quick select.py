from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n2f=Counter(nums)

        arr=[(ff, nn) for (nn, ff) in n2f.items()]

        N=len(arr)

        def qs(st, ed, k):
            pivot=arr[st+(ed-st)//2][0]
            ii, jj, kk = st, st, ed

            while jj <= kk:
                if arr[jj][0] > pivot:
                    arr[jj], arr[kk]=arr[kk], arr[jj]
                    kk-=1
                elif arr[jj][0] == pivot:
                    jj+=1
                else:
                    arr[ii], arr[jj] = arr[jj], arr[ii]
                    ii+=1
                    jj+=1

            """
            : S S S P P P P L L L L
                    i
                            j
                          k
             st                   ed
            """

            if ed-kk >= k:
                return qs(jj, ed, k)
            elif ed-ii+1 >= k:
                return pivot
            else:
                return qs(st, ii-1, k-(ed-ii+1))



        kth_freq=qs(0, N-1, k)

        res=[]
        for ff, nn in arr:
            if ff >= kth_freq:
                res.append(nn)

        return res[:k]
            
