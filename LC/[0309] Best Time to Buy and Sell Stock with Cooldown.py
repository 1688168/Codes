class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N=len(prices)

        bought=-prices[0]
        sold=0 #why this is zero instead of -math.inf?  think about ending state.
        cool_down=0 

        for ii, pp in enumerate(prices[1:], 1):
            bought_tmp=bought
            sold_tmp=sold
            cool_down_tmp=cool_down

            bought = max(bought_tmp, cool_down_tmp-pp) #s.t. to cool down restriction
            sold = max(bought_tmp+pp, sold_tmp)
            cool_down = sold_tmp

        return max(sold, 0)