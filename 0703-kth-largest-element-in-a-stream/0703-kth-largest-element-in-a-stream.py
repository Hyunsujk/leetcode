class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.record = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.record) < self.k:
                heapq.heappush(self.record, val)
        else:
            if self.record[0] < val:
                heapq.heapreplace(self.record, val)
        return self.record[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)