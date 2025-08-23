class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],x[1]))

        meetings = []
        
        for interval in intervals:
            if meetings and meetings[0] <= interval[0]:
                heapq.heappop(meetings)
            
            heapq.heappush(meetings, interval[1])
        
        return len(meetings)