class BloomFilter:
    """Bloom Filter"""
    def __init__(self, size, k):
        """
        Initialize a BloomFilter object.

        Parameters:
            size (int): The number of bits in the bit array.
            k (int): The number of hash functions to use.

        """
        self.size = size
        self.k = k
        self.bit_array = [False] * self.size

    def add(self, item):
        """
        Add an item to the BloomFilter.

        Parameters:
            item (any): The item to add to the filter.

        """
        for i in range(self.k):
            self.bit_array[hash(item, i) % self.size] = True

    def __contains__(self, item):
        """
        Check if an item is possibly in the BloomFilter.

        Parameters:
            item (any): The item to check for in the filter.

        Returns:
            bool: True if the item is possibly in the filter, False if it is definitely not.

        """
        for i in range(self.k):
            if not self.bit_array[hash(item, i) % self.size]:
                return False
        return True

    def __len__(self):
        return sum(self.bit_array)
    

import hashlib

def hash(item, i):
    """
    Return a hash of the given item, with an offset of the given integer i.

    Parameters:
        item (any): The item to hash.
        i (int): The offset to add to the hash.

    Returns:
        int: A hash of the item, with the offset added.

    """
    return int(hashlib.sha256(str(item).encode()).hexdigest(), 16) + i

    