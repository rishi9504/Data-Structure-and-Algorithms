class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * self.size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        self.table[index] = key

    def search(self, key):
        index = self.hash(key)
        return self.table[index]

    def delete(self, key):
        index = self.hash(key)
        self.table[index] = None

H = HashTable(5)
H.insert(10)
H.insert(20)
H.insert(30)
print(H.search(20))
H.delete(20)
print(H.search(20))        