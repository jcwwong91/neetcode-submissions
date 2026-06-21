class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 1:
            return 0


        hold = -prices[0]
        sell = 0
        d2 = 0
       
        for i in range(1, len(prices)):
            p = prices[i]

            prev_hold = hold
            prev_sell = sell

            hold = max(prev_hold, d2 - p)
            sell = prev_hold + p
            d2 = max(d2, prev_sell)

        return max(sell, d2)
            



        

        