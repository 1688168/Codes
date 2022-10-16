class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        M=pow(10, 9)+7
        ans=[]

        # find the power array
        def bsearch(nn): # find the larget power of 2 number which is less than N
            ll, rr, aa = 0, 31, -1

            while ll <= rr:
                mm=ll+(rr-ll)//2

                if pow(2, mm) <= nn:
                    ans=mm
                    ll=mm+1
                else:
                    rr=mm-1
            return ans

        nn=n
        pow_arr=[]
        while nn > 0:
            ni = bsearch(nn)
            pow_arr.append(pow(2, ni))
            nn -= pow_arr[-1]

        pow_arr.reverse()

        pow_product=[0]*len(pow_arr)

        pow_product[0]=pow_arr[0]
        for ii in range(1, len(pow_arr)):
            pow_product[ii]=(pow_product[ii-1])*(pow_arr[ii])

        # return product of the query into an array

        pow_product = [1]+pow_product
        for ss, ee in queries:
            ans.append((pow_product[ee+1]//pow_product[ss])%M)

        return ans
