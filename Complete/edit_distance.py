class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(word1):
                return len(word2) - j
            elif j >= len(word2):
                return len(word1) - i
            
            if word1[i] == word2[j]:
                ops = dfs(i + 1, j + 1)
            else:
                # insert
                ops = 1 + dfs(i, j + 1)
                # del
                ops = min(ops, 1 + dfs(i + 1, j))
                # replace
                ops = min(ops, 1 + dfs(i + 1, j + 1))

            memo[(i, j)] = ops
            return ops
        
        return dfs(0,0)
            
