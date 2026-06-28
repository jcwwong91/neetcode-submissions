class FreqStack:

    def __init__(self):
        self.data = list()
        self.count = dict()
        

    def push(self, val: int) -> None:
        self.data.append(val)
        self.count[val] = self.count.get(val, 0) + 1
        

    def pop(self) -> int:
        heap = list()
        rcount = dict()
        for k, v in self.count.items():
            if v not in rcount:
                rcount[v] = set()
            rcount[v].add(k)
        for k, v in rcount.items():
            heapq.heappush_max(heap, (k, v))
        _, elems = heapq.heappop_max(heap)
        
        ret = None
        tstack = list()
        while self.data:
            v = self.data.pop()
            if v in elems:
                ret = v
                break
            tstack.append(v)
        while tstack:
            self.data.append(tstack.pop())
        
        self.count[ret] -= 1
        return ret
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()