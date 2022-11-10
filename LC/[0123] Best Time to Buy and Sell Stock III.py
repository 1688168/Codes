class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        * 4 states
        hold1[k]: max( -price[k], hold1[k-1],) # the profit carried from earlier purchase or purchased today (-p profit)
        sold1[k]: max(hold[k-1]+p, sold1[k-1]) # selling stock1 today or already sold before today
        hold2: max(sold1[k-1]-p, hold2[k-1]) # first stock must be sold before purchasing next, or stock 2 already
               purchased before today
        sold2: max(hold2[k-1]+p, sold2[k-1])

        return max(sold1[n-1], sold2[n-2]), if youc an sell on last day, just sell it to capture any profit
        """

        hold1=float('-inf')
        sold1=0
        hold2=float('-inf')
        sold2=0

        for p in prices:
            hold1_tmp=hold1
            sold1_tmp=sold1
            hold2_tmp=hold2
            sold2_tmp=sold2

            hold1 = max(-p, hold1_tmp)
            sold1 = max(p+hold1_tmp, sold1_tmp)
            hold2 = max(-p+sold1_tmp, hold2_tmp)
            sold2 = max(p+hold2_tmp, sold2_tmp)

        return max(sold1, sold2)
        
