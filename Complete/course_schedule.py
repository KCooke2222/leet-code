class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_reqs = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            pre_reqs[a].append(b)

        visit = set()
        def dfs(i):
            if i in visit:
                return False
            if pre_reqs[i] == []:
                return True
            

            visit.add(i)

            for course in pre_reqs[i]:
                if not dfs(course):
                    return False
            visit.remove(i)
            pre_reqs[i] = []
            return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        return True