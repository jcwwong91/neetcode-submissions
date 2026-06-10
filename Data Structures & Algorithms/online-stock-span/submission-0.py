class StockSpanner:

    def __init__(self):
        self.stack = list()
        

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append((price, 1))
            return 1
        
        span = 1
        while self.stack:
            old_price, old_span = self.stack[-1]
            if old_price > price:
                break
            span += old_span
            self.stack.pop()
        self.stack.append((price, span))
        return span

            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)