class MyHashMap:

    def __init__(self):
        self.size = 9973
        self.data = [None] * self.size
        

    def put(self, key: int, value: int) -> None:
        k = key % self.size
        if not self.data[k]:
            self.data[k] = list()
        for i in range(len(self.data[k])):
            kk, vv = self.data[k][i]
            if kk == key:
                self.data[k][i] = (key, value)
                return
        self.data[k].append((key, value))
        

    def get(self, key: int) -> int:
        k = key % self.size
        if not self.data[k]:
            return -1
        for (kk, vv) in self.data[k]:
            if kk == key:
                return vv
        return -1
        

    def remove(self, key: int) -> None:
        k = key % self.size
        if not self.data[k]:
            return
        # print(self.data[k])
        for i in range(len(self.data[k])):
            # print(i, self.data[k])
            kk, vv = self.data[k][i]
            if kk == key:
                self.data[k].pop(i)
                break
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)