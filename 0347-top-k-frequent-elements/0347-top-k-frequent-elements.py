class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for num, f in freq.items():
            heapq.heappush(heap, (-f, num))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
    
        return res
