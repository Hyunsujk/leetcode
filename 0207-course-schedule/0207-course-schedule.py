class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        taking = set()
        taken = set()

        def noCycle(c):
            if c in taking:
                return False
            if c in taken:
                return True

            taking.add(c)
            for prereq in prereqs[c]:
                if not noCycle(prereq):
                    return False
            taking.remove(c)
            taken.add(c)

            return True
        
        for c in range(numCourses):
            if not noCycle(c):
                return False
        return True

        