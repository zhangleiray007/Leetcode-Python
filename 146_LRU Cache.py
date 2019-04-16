class LRUCache:

    def __init__(self, capacity: int):
        LRUCache.capacity = capacity
        LRUCache.length = 0
        LRUCache.dict = collections.OrderedDict() 

    def get(self, key: int) -> int:
        try:
            value = LRUCache.dict[key]
            del LRUCache.dict[key]
            LRUCache.dict[key] = value
            return value
        except:
            return -1

    def put(self, key: int, value: int) -> None:
        try:
            del LRUCache.dict[key]
            LRUCache.dict[key] = value
        except:
            if LRUCache.length == LRUCache.capacity:
                LRUCache.dict.popitem(last = False)
                LRUCache.length -= 1
            LRUCache.dict[key] = value
            LRUCache.length +=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:
        # dictionary + doubly linked list, see the picture in http://www.programcreek.com/2013/03/leetcode-lru-cache-java/
    class Node:
        def __init__(self, key, value):
            self.prev = None
            self.key = key
            self.value = value
            self.next = None

    def __init__(self, capacity: int):
        self.capacity, self.dict = capacity, {}
        self.head, self.tail = self.Node('head', 'head'), self.Node('tail', 'tail') # dummy head node and dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            self.insertNodeAtFirst(self.unlinkNode(self.dict[key]))
            return self.dict[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.insertNodeAtFirst(self.unlinkNode(self.dict[key]))
            self.dict[key].value = value
        else:
            if len(self.dict) >= self.capacity: # remove the least recently used element
                del self.dict[self.unlinkNode(self.tail.prev).key]
            self.dict[key] = self.Node(key, value)
            self.insertNodeAtFirst(self.dict[key])
    def unlinkNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        return node
         
    def insertNodeAtFirst(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)