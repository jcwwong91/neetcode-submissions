class MyHashSet:

    def __init__(self):
        self.data = [False] * 100000

    def add(self, key: int) -> None:
        key = key % 100000
        self.data[key] = True
        

    def remove(self, key: int) -> None:
        key = key % 100000
        self.data[key] = False
        

    def contains(self, key: int) -> bool:
        key = key % 100000
        return self.data[key]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)