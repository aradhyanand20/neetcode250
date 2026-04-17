class MyHashMap:

    def __init__(self):

        self.size = 1000
        self.arrays = [[] for _ in range(self.size)]

        
    def hash(self,key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)

        for i, (k,v) in enumerate(self.arrays[index]):
            if k == key:
                self.arrays[index][i] =(key,value)
                return
        self.arrays[index].append((key,value))

        

    def get(self, key: int) -> int:
        index = self.hash(key)
        for k,v in self.arrays[index]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        for i, (k,v) in enumerate(self.arrays[index]):
            if k == key:
                del self.arrays[index][i]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)