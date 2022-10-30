from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        top k -> quick select
        S S S U U U L L L
        """
        #1 get freq count
        ctr=Counter(nums)
        arr=[(kk, vv) for kk, vv in ctr.items()]

        def quick_select(st, ed, k):
            pivot=arr[st+(ed-st)//2][1]
            ii, jj, kk = st, st, ed

            """
            SSSSPPPLLL
            """
            while jj <= kk:
                if arr[jj][1] > pivot:
                    arr[jj], arr[kk]=arr[kk],arr[jj]
                    kk -= 1
                elif arr[jj][1]== pivot:
                    jj += 1
                else:
                    arr[ii], arr[jj]=arr[jj],arr[ii]
                    ii+=1
                    jj+=1

            """
                       4  5 6 7 8
            S S S P P P   L L L L
            st    ii  kk  jj    ed
            """
            if ed-kk >= k:
                return quick_select(jj, ed, k)
            elif ed-ii+1 >= k:
                return pivot
            else:
                return quick_select(st, ii-1, k-(ed-ii+1))


        N=len(arr)
        ff = quick_select(0, N-1, k)

        #kk is the kth largest freq

        res=[]
        for (kk, vv) in arr:
            if vv >= ff: res.append(kk)

        return res[:k]
