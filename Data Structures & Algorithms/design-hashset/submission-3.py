class MyHashSet:

    def __init__(self):
        self.data = [0] * math.ceil(1000000 / 32)

    def add(self, key: int) -> None:
        self.data[key // 32] |= 1 << (key % 32)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.data[key // 32] ^= 1 << (key % 32)

    def contains(self, key: int) -> bool:
        mask = 1 << (key % 32)
        return self.data[key //32] & mask != 0
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)