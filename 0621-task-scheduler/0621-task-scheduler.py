class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        awaiting_tasks = [-c for c in count.values()]
        heapq.heapify(awaiting_tasks)

        cooltime = deque()
        time = 0

        while awaiting_tasks or cooltime:
            time += 1

            if awaiting_tasks:
                c = heapq.heappop(awaiting_tasks) + 1
                if c != 0:
                    cooltime.append((time + n, c))
            
            if cooltime and cooltime[0][0] == time:
                c = cooltime.popleft()[1]
                heapq.heappush(awaiting_tasks, c)
        
        return time
