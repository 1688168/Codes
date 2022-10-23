class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product=[]
        sufix_product=[]

        for n in nums:
            if len(prefix_product)==0:
                prefix_product.append(n)
            else:
                prefix_product.append(prefix_product[-1]*n)

        for n in reversed(nums):
            if len(sufix_product)==0:
                sufix_product.append(n)
            else:
                sufix_product.append(sufix_product[-1]*n)

        sufix_product.reverse()

        res=[]

        N=len(nums)
        for ii in range(N):
            if ii ==0:
                res.append(sufix_product[1])
            elif ii == N-1:
                res.append(prefix_product[-2])
            else:
                res.append(prefix_product[ii-1]*sufix_product[ii+1])
        return res
        
