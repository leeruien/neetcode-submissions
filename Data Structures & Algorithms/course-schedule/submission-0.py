class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            
            preMap[course].append(pre)
        visitSet = set()
        def check_pre(course):

            if course in visitSet: return False
            if preMap[course] == []: return True
            visitSet.add(course)
            for pre in preMap[course]:
                if not check_pre(pre): return False
            visitSet.remove(course)
            preMap[course] = []
            return True
        for course in range(numCourses):
            if not check_pre(course): return False
        return True

            
