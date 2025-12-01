class Allocator:

    def __init__(self, n: int):
        self.free = [(0, n-1)]
        self.allocated = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        for idx, (l, r) in enumerate(self.free):
            if r - l + 1 >= size:
                start = l
                end = l + size - 1

                if end == r:
                    self.free.pop(idx)
                else:
                    self.free[idx] = (end+1, r)
                self.allocated[mID].append((start, end))

                return start
        return -1
        

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for start, end in self.allocated[mID]:
            freed += (end - start + 1)
            self._insert_interval(start, end)
        
        self.allocated[mID] = []
        
        return freed
    
    def _insert_interval(self, l, r):
        idx = bisect_left(self.free, (l, r))

        if idx > 0 and self.free[idx-1][1] + 1 >= l:
            idx -= 1
            l = min(self.free[idx][0], l)
            r = max(self.free[idx][1], r)
            self.free.pop(idx)
        
        while idx < len(self.free) and self.free[idx][0] <= r + 1:
            l = min(self.free[idx][0], l)
            r = max(self.free[idx][1], r)
            self.free.pop(idx)

        self.free.insert(idx, (l, r))
        
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)