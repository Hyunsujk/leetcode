class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        k = r

        while l <= r:
            total = 0
            mid = (r+l)//2

            for p in piles:
                total += p//mid
                if p % mid != 0:
                    total += 1
            
            if total <= h:
                k = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return k