from bisect import bisect_left
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        1. sort 
        2. binary search the prefix 
        3. find top 3 matched words
        """
        products.sort() # nlogn

        prefix=""
        res=[]
        N = len(products)
        for c in searchWord:
            prefix+=c
            idx = bisect_left(products, prefix)

            matched=[]
            for ii in range(idx, min(idx+3, N)):
                if products[ii][:len(prefix)] == prefix:
                    matched.append(products[ii])
                else:
                    break
            res.append(matched)
        
        return res
            

        