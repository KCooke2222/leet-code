class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key to node

        # left = lru, right=mru
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # set to mru
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # add or update - either way mru
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # remove lru from cache and linked list
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



