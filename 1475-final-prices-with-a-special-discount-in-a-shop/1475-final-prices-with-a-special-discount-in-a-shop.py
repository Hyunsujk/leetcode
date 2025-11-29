class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = [0] * len(prices)
        for idx, price in enumerate(prices):
            while stack and stack[-1][1] >= price:
                i, p = stack.pop()
                discount = p - price
                res[i] = discount
            stack.append((idx, price))
        
        while stack:
            i, p = stack.pop()
            res[i] = p
        
        return res
