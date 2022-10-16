class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res=[]
        N=len(pref)
        acc=0
        for ii in range(N):
            if ii == 0:
                res.append(pref[ii])
                acc ^= pref[ii]
            else:
                res.append(pref[ii]^acc)
                acc ^= res[-1]
            #print(" acc: ", acc)



        return res
