class MyCircularQueue:

    def __init__(self, k: int):
        self.data = [None] * k
        self.front = None
        self.end = None
        self.ptr = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.data[self.ptr] = value
        if self.front is None:
            self.front = self.ptr
        self.end = self.ptr
        self.ptr = 0 if self.ptr == len(self.data) -1 else self.ptr + 1
        print("enqueue", value)
        return True

    def deQueue(self) -> bool:
        if self.front is None:
            return False
        if self.front == self.end:
            self.front = None
            self.end = None
            return True
        print("dequeue", self.data[self.front])
        self.front = 0 if self.front == len(self.data) -1 else self.front + 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.end]
        

    def isEmpty(self) -> bool:
        return self.front is None

    def isFull(self) -> bool:
        if self.front is None:
            return False
        return self.front == 0 and self.end == len(self.data)-1 or self.end == self.front-1
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()