class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        r = []
        for num in nums:
            if len(r) < k:
                heapq.heappush(r, num)
            else:
                if r[0] < num:
                    heapq.heapreplace(r, num)
        
        return r[0]