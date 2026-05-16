class Node:
    def __init__(self, val=None, key=None):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def update_head(self, node):
        # Move to node to head
        prevHead = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = prevHead
        prevHead.prev = node
        
    def check_to_evict(self):
        if len(self.cache) == self.capacity:
            self.remove(self.tail.prev, True)
        

    def remove(self, node, removeFromCache=False):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        node.next = None
        node.prev = None

        if removeFromCache:
            del self.cache[node.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # break linkage
        self.remove(node)
        # Update head
        self.update_head(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.update_head(node)
        else:
            self.check_to_evict()
            node = Node(key = key, val = value)
            self.update_head(node)
            self.cache[key] = node
        


        
