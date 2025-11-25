class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:      
        next_classes = defaultdict(list)
        prereq_count = [0] * numCourses
        for c, prereq in prerequisites:
            next_classes[prereq].append(c)
            prereq_count[c] += 1

        q = deque([i for i in range(numCourses) if prereq_count[i] == 0])

        order = []
    
        while q:
            course = q.popleft()
            order.append(course)

            for next_course in next_classes[course]:
                prereq_count[next_course] -= 1
                if prereq_count[next_course] == 0:
                    q.append(next_course)
        
        return order if len(order) == numCourses else []

                

        