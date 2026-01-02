class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        # dfs returns if false if cycle, 
        # and gets visit set to compare with the list
        def dfs(i, parent):
            if i in visit:
                return False
            
            visit.add(i)

            for j in adj[i]:
                if j == parent:
                    continue
                if not dfs(j, i):
                    return False

            return True

        cycle_check = dfs(0, None)
        connected_check = len(visit) == n

        return cycle_check and connected_check