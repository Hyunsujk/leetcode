class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(list)
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            prereqs[prereq].append(course)
            indegree[course] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        while queue:
            c = queue.popleft()
            visited += 1

            for prereq in prereqs[c]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    queue.append(prereq)
        
        return visited == numCourses