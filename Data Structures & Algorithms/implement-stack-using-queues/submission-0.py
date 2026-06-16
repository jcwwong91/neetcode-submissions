class MyStack:

    def __init__(self):
        self.data = list()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        # print("1", self.data)
        for i in range(len(self.data)-1):
            v = self.data.pop(0)
            self.data.append(v)
        # print("2",self.data)
        return self.data.pop(0)

    def top(self) -> int:
        v = self.pop()
        self.data.append(v)
        return v
        

    def empty(self) -> bool:
        return len(self.data) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()