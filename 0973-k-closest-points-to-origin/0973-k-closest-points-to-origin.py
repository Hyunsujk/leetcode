class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for x, y in points:
            d = math.sqrt(x**2 + y**2)
            if len(distance) < k:
                heapq.heappush(distance, (-d, [x, y]))
            else:
                if -distance[0][0] > d:
                    heapq.heapreplace(distance, (-d, [x, y]))
        
        return [p for d, p in distance]