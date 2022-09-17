from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        * count freq: T: O(N), S:O(M) M as the unique words
        * sort by (freq, word): mlogm
        * output first k: O(K)
        # top first k --> quick select --> avg: O(N)
        * count freq into array
        * quickselect for k
        * output fist k
        """
        ctr=Counter(words)
        #print("counter: ", ctr)
        ws=[(kk, vv) for kk, vv in ctr.items()]

        #print(" ws: ", ws)

        res=[]
        def quickselect(st, ed, k):
            p=ws[st + (ed-st)//2][1]

            ii, jj, kk = st, st, ed

            while jj <= kk:
                if ws[jj][1] > p:
                    ws[jj], ws[kk]=ws[kk], ws[jj]
                    kk-=1
                elif ws[jj][1] < p:
                    ws[ii], ws[jj]=ws[jj], ws[ii]
                    ii+=1
                    jj+=1
                else:
                    jj+=1

            """
            SSSPPPPPLLL
               i   kj
            """

            if ed-kk>=k:
                return quickselect(jj, ed, k)
            elif ed-ii+1 >= k:
                return p
            else:
                return quickselect(st, ii-1, k-(ed-ii+1))



        kth=quickselect(0, len(ws)-1, k)

        #print("kth: ", kth)
        for kk, vv in ws:
            if vv >= kth:
                res.append((vv, kk))


        res.sort(key=lambda x: (-x[0], x[1]))

        #print(res)


        return [vv for kk, vv in res[:k]]
