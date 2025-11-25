class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        for c, prereq in prerequisites:
            adjList[c].append(prereq)
        
        taking = set()
        taken = set()

        def noCycle(course):
            if course in taking:
                return False
            if course in taken:
                return True
            
            taking.add(course)
            for prereq in adjList[course]:
                if not noCycle(prereq):
                    return False
            taking.remove(course)
            taken.add(course)
            return True
        
        for i in range(numCourses):
            if not noCycle(i):
                return False
        return True