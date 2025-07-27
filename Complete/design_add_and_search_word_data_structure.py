class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        cur.endOfWord = True
        

    def search(self, word: str) -> bool:
        def expand(i, root):
            cur = root

            for c in range(i, len(word)):
                char = word[c]

                if char == '.':
                    for child in cur.children.values():
                        if expand(c+1, child):
                            return True
                    return False
                else:
                    if char not in cur.children:
                        return False
                    cur = cur.children[char]
                
            return cur.endOfWord

        return expand(0, self.root)
        
        
