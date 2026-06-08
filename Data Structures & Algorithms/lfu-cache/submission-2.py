class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.frequency = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.data = dict()
        self.head = None
        

    def get(self, key: int) -> int:
        print("get", key)
        self.printEvictionQueue()
        node = self.data.get(key)
        if not node:
            return -1

        prev = node.prev
        node.frequency += 1
        n = node.next

        while n and n.frequency <= node.frequency:
            prev = n
            n = n.next
        
        if self.head == node:
            self.head = node.next
        self.remove(node)
        self.insert(prev, node, n)
        self.printEvictionQueue()
        return node.value

        
    def put(self, key: int, value: int) -> None:
        print("put", key, value)
        self.printEvictionQueue()
        if len(self.data) == self.cap:
            self.evict()

        node = self.data.get(key)
        if not node:
            node = Node(key, value)
            self.data[key] = node
        else:
            node.value = value
            node.frequency += 1
            return

        if not self.head:
            self.head = node
            self.printEvictionQueue()
            return 
        
        prev = None
        n = self.head
        while n and n.frequency == 1:
            prev = n
            n = n.next
        
        nxt = n
        if prev:
            nxt = prev.next
        self.insert(prev, node, nxt)
        self.printEvictionQueue()

    def evict(self):
        if self.head is None:
            raise Exception("no head to evict")

        toEvict = self.head
        self.head = toEvict.next
        del(self.data[toEvict.key])
        print("evicted", toEvict.key)
        

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        
        node.prev = None
        node.next = None

        if node == self.head:
            self.head = nxt

        if prev:
            prev.next = nxt        
        if nxt:
            nxt.prev = prev

    def insert(self, prev, node, nxt):
        if prev and nxt and (prev.next != nxt or nxt.prev != prev):
            raise Exception("invalid")

        if prev:
            prev.next = node
        node.prev = prev

        if nxt:
            nxt.prev = node
        node.next = nxt

        if nxt == self.head:
            self.head = node

    def printEvictionQueue(self):
        s = "eq = "
        n = self.head
        while n:
            s += f"{n.key}({n.frequency}) - "
            n = n.next
        print(s)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)