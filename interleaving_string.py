class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        # i s1 | j s2
        def dfs(i, j):
            k = i + j
            if k == len(s3):
                return i == len(s1) and j == len(s2)
            
            if (i, j) in memo:
                return memo[(i,j)]

            ans = False
            if i < len(s1) and s1[i] == s3[k]:
                ans = dfs(i+1, j)

            if j < len(s2) and  s2[j] == s3[k]:
                ans = dfs(i, j+1)

            memo[(i,j)] = ans
            return ans

        return dfs(0, 0)

            
