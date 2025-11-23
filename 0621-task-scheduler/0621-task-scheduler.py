class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        task_q = [-c for c in count.values()]
        heapq.heapify(task_q)

        time = 0
        cooltime = deque()

        while task_q or cooltime:
            time += 1

            if task_q:
                c = heapq.heappop(task_q) + 1
                if c != 0:
                    cooltime.append((time+n, c))
            
            if cooltime and cooltime[0][0] == time:
                c = cooltime.popleft()[1]
                heapq.heappush(task_q, c)
        
        return time