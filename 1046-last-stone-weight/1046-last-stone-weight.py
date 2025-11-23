class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            diff = abs(stone1-stone2)
            if diff != 0:
                heapq.heappush(max_heap, -diff)
        
        return -max_heap[0] if len(max_heap) > 0 else 0