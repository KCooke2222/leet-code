class TrieNode:
    def __init__(self):
       self.children = {}
       self.isWord = False

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create trie w/ words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        rows = len(board)
        cols = len(board[0])
        
        res, visit = set(), set()

        def dfs(r, c, node, word):
            # many base cases
            if (r < 0 or c < 0 or
                r == rows or c == cols or
                (r,c) in visit or board[r][c] not in node.children):
                return
            
            # mark visit
            visit.add((r,c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            
            for ra, ca in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr = r + ra
                nc = c + ca

                dfs(nr, nc, node, word)

            visit.remove((r,c))
           

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)