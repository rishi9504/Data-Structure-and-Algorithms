# Hashing is a technique used to map data of arbitrary size to fixed size values, typically integers. It is used in various applications, including data structures, databases, and cryptography. In the context of programming, hashing is often used to quickly search for data in a data structure, such as a hash table or a hash set.

# Hashing works by taking an input value, called the key, and applying a hash function to it. The hash function takes the key and produces a hash value, which is typically an integer. The hash value is used to locate the data in a data structure, such as a hash table or a hash set.

# The key characteristics of a good hash function are:

# - Deterministic: Given the same input, the hash function always produces the same output.
# - Fast: The hash function should be computationally efficient.
# - Uniform: The hash function should distribute the input values evenly across the output range.
# - No collisions: A collision occurs when two different input values produce the same hash value. A good hash function should minimize collisions.

# In Python, the built-in `hash()` function can be used to compute the hash value of an object. However, the resulting hash value is specific to the Python interpreter and may not be portable across different systems or versions of Python. For portable hashing, it is recommended to use a well-known hash function, such as MD5 or SHA-256, or a dedicated hashing library, such as `hashlib` in Python.



# A hash function is a mathematical function that takes an input value (called the key) and produces a fixed-size output value (called the hash value or digest). The output value is typically an integer, and it is designed to be unique for each unique input value.

# A good hash function should have the following properties:

# 1. **Deterministic**: Given the same input, the hash function always produces the same output.
# 2. **Fast**: The hash function should be computationally efficient.
# 3. **Uniform**: The hash function should distribute the input values evenly across the output range.
# 4. **No collisions**: A collision occurs when two different input values produce the same hash value. A good hash function should minimize collisions.

# Hash functions are often used in data structures such as hash tables, where they are used to map keys to indices of a backing array. They are also used in cryptography, where they are used to create digital signatures and verify the integrity of data.

# Some common examples of hash functions include:

# * **MD5** (Message-Digest Algorithm 5): a widely used hash function that produces a 128-bit hash value.
# * **SHA-256** (Secure Hash Algorithm 256): a widely used hash function that produces a 256-bit hash value.
# * **CRC-32** (Cyclic Redundancy Check 32): a hash function that produces a 32-bit hash value, often used for error detection in data transmission.

# In Python, the built-in `hash()` function can be used to compute the hash value of an object. However, this function is not suitable for cryptographic purposes, as it is designed for use in hash tables and is not secure against collisions.



# Collision resolution techniques are methods used to handle collisions that occur when two different input values produce the same hash value. Collisions can occur in hash tables, hash sets, and other data structures that use hash functions to map keys to indices.

# Here are some common collision resolution techniques:

# 1. **Chaining**: In this technique, each bucket (or slot) in the hash table contains a linked list of entries that hash to the same index. When a collision occurs, the new entry is simply added to the end of the linked list.
# 2. **Open Addressing**: In this technique, when a collision occurs, the hash table searches for the next available slot in the table to store the new entry. There are several variants of open addressing, including:
# 	* **Linear Probing**: The hash table searches for the next available slot by probing the table linearly (i.e., by incrementing the index by 1).
# 	* **Quadratic Probing**: The hash table searches for the next available slot by probing the table quadratically (i.e., by incrementing the index by a quadratic function).
# 	* **Double Hashing**: The hash table uses a second hash function to probe the table.
# 3. **Resizing**: When the hash table becomes too full (i.e., the load factor exceeds a certain threshold), the table is resized to a larger size, and all the entries are rehashed.
# 4. **Cuckoo Hashing**: In this technique, when a collision occurs, the new entry "kicks out" one of the existing entries in the table, which is then moved to a different location in the table.
# 5. **Hopscotch Hashing**: In this technique, when a collision occurs, the new entry is stored in a nearby location in the table, and the existing entry is "hopped" to a different location.

# Each collision resolution technique has its own trade-offs in terms of time and space complexity, and the choice of technique depends on the specific use case and requirements.

# Bloom Filter is a data structure that is used to efficiently determine if an element is present in a collection. It is commonly used in search engines to determine if an element is relevant to the query.

# Here is an example of using Bloom Filter in Python:

# ```python
# from bloom_filter import BloomFilter

# # Create a Bloom Filter with 1000 elements
# bf = BloomFilter(1000)

# # Add elements to the Bloom Filter
# bf.add("apple")
# bf.add("banana")

# # Check if an element is present in the Bloom Filter
# print("apple" in bf)
# print("orange" in bf)
# ```

