class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for c, prereq in prerequisites:
            adjList[c].append(prereq)

        taken = set()
        taking = set()

        def dfs(course):
            if course in taking:
                return False
            if course in taken:
                return True
            
            taking.add(course)
            
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False

            taking.remove(course)
            taken.add(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True