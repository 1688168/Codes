
################
# 20230114
################
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        : nums - ints
        : Time - O(N)
        : preprod - array of product for all numbers before current index
        : postprod - array of product for all numbers after current index
        : answer[ii]=preprod[ii]*postprod[ii]
        : Space - O(2n) -> o(N)
        : Time - O(N)
        """
        N=len(nums)
        preprod=[1]*N
        postprod=[1]*N
        ans=[]

        for ii in range(1, N):
            """
            1 = 1*n0
            2 = n1*1

            
            """
            preprod[ii]=preprod[ii-1]*nums[ii-1]
            postprod[N-ii-1]=postprod[N-ii]*nums[N-ii]
        
        for ii in range(N):
            ans.append(preprod[ii]*postprod[ii])
        
        return ans

################
# 20221104
################

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_prod=[]
        post_prod=[]

        N=len(nums)
        #preprod
        for ii in range(N):
            if ii==0:
                pre_prod.append(1)
            else:
                pre_prod.append(pre_prod[-1]*nums[ii-1])


        for ii in reversed(range(N)):
            if ii==N-1:
                post_prod.append(1)
            else:
                post_prod.append(post_prod[-1]*nums[ii+1])

        # print("pre: ", pre_prod)
        # print("post: ", post_prod)


        post_prod.reverse()


        res=[]

        for ii in range(len(nums)):
            res.append(pre_prod[ii]*post_prod[ii])

        return res

#==============================

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
