class Node:
 def __init__(self,val):
    self.val = val
    self.next = None



class MyHashSet:

    

    def __init__(self):
        self.size = 1000
        self.bucket = [None] * self.size

    def hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        h = self.hash(key)

        if self.bucket[h] is None:
            self.bucket[h] = Node(key)
            return
        
        curr = self.bucket[h]
        
        while True:
            if curr.val == key:
                return
            if curr.next is None:
                break
            curr = curr.next
        curr.next = Node(key)


        
        

    def remove(self, key: int) -> None:
        h = self.hash(key)
        self.bucket[h] = Node(key)
        curr = self.bucket[h]
        prev = None

        while curr:
            if curr.val == key:
                if prev:
                  prev.next = curr.next
                else:
                  self.bucket[h] = curr.next
            return
           
        prev = curr
        curr = curr.next
        

    def contains(self, key: int) -> bool:
        h = self.hash(key)
        curr = self.bucket[h]
        while curr:
            if curr.val == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)