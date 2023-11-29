#------------Problem: 207------------

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqMap = {i: [] for i in range(numCourses)}
        for course, req in prerequisites:
            reqMap[course].append(req)

        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            if reqMap[course] == []:
                return True
            
            visiting.add(course)

            for neighbor in reqMap[course]:
                if not dfs(neighbor):
                    return False
            visiting.remove(course)
            reqMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True