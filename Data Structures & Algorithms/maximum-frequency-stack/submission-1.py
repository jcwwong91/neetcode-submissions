class FreqStack:

    def __init__(self):
        self.count = dict()
        self.freq_stack = [list()]
        self.max_freq = 0
        

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        self.max_freq = max(self.max_freq, self.count[val])

        if self.max_freq >= len(self.freq_stack):
            self.freq_stack.append(list())

        self.freq_stack[self.count[val]].append(val)


    def pop(self) -> int:   
        val = self.freq_stack[self.max_freq].pop()
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1
        
        self.count[val] -= 1

        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()