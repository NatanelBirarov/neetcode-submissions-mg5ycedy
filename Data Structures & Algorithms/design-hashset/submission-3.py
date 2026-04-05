class MyHashSet:

    def __init__(self):
        self.capacity = 1000000
        self.table = [[] for _ in range(self.capacity)]

    def _hash(self, key) -> None:
        hash_value = 0
        if isinstance(key, int):
            hash_value = key
        else:
            prime = 31  # Using a prime helps distribute values more evenly
            
            for char in key:
                # ord(char) gets the ASCII/Unicode value (e.g., 'A' is 65)
                hash_value = (hash_value * prime) + ord(char)
        
        # Applying the modulo operation
        return hash_value % self.capacity

    def add(self, key: int) -> None:
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        return key in self.table[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)