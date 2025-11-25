class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        next_classes = defaultdict(list)
        prereq_count = [0] * numCourses

        for course, prereq in prerequisites:
            next_classes[prereq].append(course)
            prereq_count[course] += 1
        
        q = deque([i for i in range(numCourses) if prereq_count[i] == 0])

        taken = 0

        while q:
            course = q.popleft()
            taken += 1

            for next_course in next_classes[course]:
                prereq_count[next_course] -= 1
                if prereq_count[next_course] == 0:
                    q.append(next_course)
        
        return True if taken == numCourses else False
                