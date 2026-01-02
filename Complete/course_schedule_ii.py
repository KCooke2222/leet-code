class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_reqs = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            pre_reqs[a].append(b)

        res = []

        visit = set()
        visited = set()
        def dfs(i):
            if i in visit:      # cycle
                return False
            if i in visited:    # already done
                return True
            

            visit.add(i)

            for course in pre_reqs[i]:
                if not dfs(course):
                    return False
            visit.remove(i)
            visited.add(i)

            # add here once done processing
            # prereqs will be placed first then the node
            res.append(i)

            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        return res   
            
