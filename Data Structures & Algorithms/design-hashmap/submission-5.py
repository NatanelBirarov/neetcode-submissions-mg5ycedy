class ListNode:
    def __init__(self, key: int = -1, value: int = -1, next = None):
        self.key = key
        self.val = value
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def _hash(self, key):
        return key % len(self.map)

    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        index = self._hash(key)
        cur = self.map[index]
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
        

    def remove(self, key: int) -> None:
        index = self._hash(key)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)



class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False