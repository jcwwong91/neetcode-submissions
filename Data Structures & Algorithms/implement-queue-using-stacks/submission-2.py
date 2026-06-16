class MyQueue:

    def __init__(self):
        self.stack = list()
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = list()
        # print("pop1", self.stack)
        for _ in range(len(self.stack)-1):
            temp.append(self.stack.pop())
        ret = self.stack.pop()
        for _ in range(len(temp)):
            self.stack.append(temp.pop())
        # print("pop2", self.stack)
        return ret

    def peek(self) -> int:
        temp = list()
        # print("peek1", self.stack)
        for _ in range(len(self.stack)-1):
            temp.append(self.stack.pop())
        ret = self.stack.pop()
        self.stack.append(ret)
        for _ in range(len(temp)):
            self.stack.append(temp.pop())
        # print("peek2", self.stack)
        return ret
        
    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()