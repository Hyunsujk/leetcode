class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestBuy = prices[0]
        
        for price in prices:
            if price < lowestBuy:
                lowestBuy = price
            else:
                profit = price - lowestBuy
                if profit > maxProfit:
                    maxProfit = profit
        
        return maxProfit



        