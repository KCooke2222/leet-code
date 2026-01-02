class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # just dfs to find path
        # add memoed word memo
        # visited for current path (or could use bfs)
        # take smallest path at each level of dfs

        memo = {}

        def dfs(word, visited):
            if word == endWord:
                return 1
            if word in memo:
                return memo[word]
            if word in visited:
                return float('inf')

            visited.add(word)

            # check via the chars one should be diff
            small_path = float('inf')
            for jump_word in wordList:
                diff = 0
                for c in range(len(word)):
                    if word[c] != jump_word[c]:
                        diff += 1
                if diff > 1:
                    continue
                
                path = 1 + dfs(jump_word, visited)
                small_path = min(small_path, path) 
            
            visited.remove(word)
            memo[word] = small_path
            return small_path # in case dead end return inf

        res = dfs(beginWord, set())
        return res if res != float('inf') else 0
