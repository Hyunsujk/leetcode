class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                j = stack.pop()
                prices[j] -= price
            stack.append(i)
        
        return prices