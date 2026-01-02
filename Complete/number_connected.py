class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # based on visited list
        # run dfs for each item in list increment the number if not visisted by other group

        visit = set()

        def dfs(node):
            if node in visit:
                return 0
            
            visit.add(node)

            # find the edges connected to node and dfs to connection
            for edge in edges:
                if node == edge[0]:
                    dfs(edge[1])
                elif node == edge[1]:
                    dfs(edge[0])

            return 1

        res = 0
        for node in range(n):
            res += dfs(node)

        return res