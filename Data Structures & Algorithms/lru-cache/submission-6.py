from collections import deque
class Node:
    def __init__(self, val=0, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def _handle_evict(self):
        if len(self.cache)>=self.capacity:
            currLRU = self.tail.prev
            self.tail.prev = currLRU.prev
            currLRU.prev.next = self.tail
            del self.cache[currLRU.val[1]]

    def _move_node_to_front(self, node: Node):
        # Fix border nodes from og placement
        prevNode = node.prev
        nextNode = node.next
        if prevNode and nextNode:
            prevNode.next = nextNode
            nextNode.prev = prevNode

        # store current mru
        self.mru = self.head.next
        # add node to mru position
        self.head.next = node
        node.next = self.mru
        node.prev = self.head
        # point past mru to node
        self.mru.prev = node
        return node
    
    def _create_node(self, key, val):
        newNode = Node(val = (val, key))
        self._move_node_to_front(newNode)
        self.cache[key] = newNode

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        node = self.cache[key]
        

        # update node to new LRU
        self._move_node_to_front(node)

        return node.val[0]

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self._handle_evict()
            self._create_node(key,value)
        else:
            self.cache[key].val = (value, key)
            node = self.cache[key]
            self._move_node_to_front(node)

    


        
    
       
        
