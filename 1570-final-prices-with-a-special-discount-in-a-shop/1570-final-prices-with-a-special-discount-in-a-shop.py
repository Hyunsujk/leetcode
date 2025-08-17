class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        final = [0] * len(prices)
        for i in range(len(prices)):
            final[i] = prices[i]
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    final[i] = prices[i] - prices[j]
                    break
        
        return final
        