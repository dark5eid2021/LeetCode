"""
LeetCode 706: Design a HashMap

Problem: Design a hashmap without using any built-in hash table libraries.

Implement the MyHashMap class:
- MyHashMap() initializes the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists, update the corresponding value.
- int get(int key) returns the value to which the specified key is mapped,
    or -1 if this map contains no mapping for the key.
- void remove(int key) removes the key and its corresponding value if the map contains the mapping for the 
    key.


Time Complexity: O(1) average case, O(n) worst case for all operations
Space Complexity: O(n) where n is the number of key-value pairs
"""

class MyHashMap:
    """
    HashMap implementation using chaining for collision resolution

    Key design decisions:
    1. Use array of buckets (linked lists) to handle collision operations 
    2. Simple hash function: key % bucket_count
    3. Dynamic resizing when load factor exceeds threshold
    4. Separate chaining with linked lists

    This implementation handles:
    - collisions via chaining
    - dynamic resizing 
    - load factor management
    """


    def __init__(self):
        self.bucket_count = 1000 # Initial number of buckets
        self.buckets = [[] for _ in range(self.bucket_count)]
        self.size = 0
        self.load_factor_threshold = 0.75 # keeps too many key-value pairs from being put in 1 bucket 

    def _hash(self, key): # _hash means this is a helper method — not meant to be used outside the class.
        """Simple hash function"""
        return key % self.bucket_count

    def _resize(self):
        """Resize hash table when load factor exceeds threshold"""
        old_buckets = self.buckets
        self.bucket_count *= 2 # the same as self.bucket_count = self.bucket_count * 2
        self.buckets = [[] for _ in range(self.bucket_count)]
        old_size = self.size 
        self.size = 0

        # Rehash all existinng key-value pairs
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    
    def put(self, key, value):
        """
        Insert or update key-value pair
        Steps:
        1. Find appropriate bucket using hash function
        2. Search bucket for existing key
        3. If found: update value
        4. If not found: append new pair and check for resize
        """
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        # Search for existing key in bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) # update existing
                return 
        
        # key not found, add new pair
        bucket.append((key, value))
        self.size += 1

        # check if resize is needed
        if self.size > self.bucket_count * self.load_factor_threshold:
            self._resize()
    
    def get(self, key):
        """
        Get value by key
        
        Steps:
        1. Find appropriate bucket using hash function
        2. Search bucket for key
        3. Remove if found
        """

        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for k, v in bucket:
            if k == key:
                return v 
        
        return -1
    
    def remove(self, key):
        """
        Remove key-value pair
        
        Steps:
        1. Find appropriate bucket using hash function
        2. Search bucket for key
        3. Remove if found
        """

        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= -1
                return
    
    def get_load_factor(self):
        """Helper method to check current load factor"""
        return self.size / self.bucket_count if self.bucket_count > 0 else 0
    


# Test cases
def test_hashmap():
    hashmap = MyHashMap()

    # Test basic operations
    hashmap.put(1, 1)
    hashmap.put(2, 2)
    assert hashmap.get(1) == 1
    assert hashmap.get(3) == -1

    # Test update
    hashmap.put(2, 1)
    assert hashmap.get(2) == 1

    # Test remove
    hashmap.remove(2)
    assert hashmap.get(2) == -1

    # Test collision handling (keys that hash to the same bucket)
    hashmap.put(1, 1)
    hashmap.put(1001, 2) # Assuming bucket_count=1000, this collides iwth key 1
    assert hashmap.get(1) == 1
    assert hashmap.get(1001) == 2

    print("✅ HashMap tests passed!")

def test_load_factor_and_resize():
    hashmap = MyHashMap()

    # Add many elements to trigger resize
    for i in range(800):
        hashmap.put(i, i * 2)

    print(f"Load factor after resize: {hashmap.get_load_factor():.2f}")

    # This should trigger resize 
    hashmap.put(800, 1600)

    print(f"Load factor after resize: {hashmap.get_load_factor():.2f}")
    print(f"Bucket count after resize: {hashmap.bucket_count}")

    # Verify all elements still accessible 
    for i in range(801):
        assert hashmap.get(i) == i * 2
    
    print("✅ Resize functionality works!")


if __name__ == "__main__":
    test_hashmap()
    test_load_factor_and_resize()



# Interview talking points:
"""
Key points to mention during interview:

1. CLARIFY REQUIREMENTS:
   - "What's the expected range of keys?" (affects hash function choice)
   - "Should I handle dynamic resizing?" (affects complexity)
   - "Any constraints on memory usage?" (affects bucket count)

2. DESIGN DECISIONS:
   - "I'll use separate chaining to handle collisions"
   - "Simple modulo hash function for demonstration"
   - "Dynamic resizing when load factor exceeds 0.75"

3. COLLISION RESOLUTION STRATEGIES:
   - Separate chaining (linked lists in buckets)
   - Open addressing (linear/quadratic probing, double hashing)
   - Trade-offs: memory vs cache performance

4. HASH FUNCTION CONSIDERATIONS:
   - Simple modulo for integer keys
   - For strings: polynomial rolling hash
   - Cryptographic vs non-cryptographic hash functions
   - Importance of uniform distribution

5. LOAD FACTOR MANAGEMENT:
   - Keep load factor < 0.75 for good performance
   - Resize by doubling bucket count
   - Rehash all existing elements after resize

6. TIME COMPLEXITY ANALYSIS:
   - Average case: O(1) for all operations
   - Worst case: O(n) if all keys hash to same bucket
   - Amortized O(1) with proper resizing

7. SPACE COMPLEXITY:
   - O(n) for n key-value pairs
   - Additional overhead for empty buckets
   - Trade-off between space and collision probability

8. ALTERNATIVE APPROACHES:
   - Open addressing vs chaining
   - Robin Hood hashing
   - Cuckoo hashing
   - Consistent hashing (distributed systems)

9. PRODUCTION CONSIDERATIONS:
   - Thread safety (locks, atomic operations)
   - Memory management (object pooling)
   - Cache-friendly data structures
   - Monitoring and metrics

10. FOLLOW-UP QUESTIONS:
    - "How would you handle string keys?" (string hashing)
    - "What about thread safety?" (locks, lock-free approaches)
    - "How to optimize for cache performance?" (open addressing)
    - "Design for distributed systems?" (consistent hashing)

This problem tests:
- Understanding of hash table internals
- Knowledge of collision resolution strategies
- Algorithm analysis (time/space complexity)
- System design thinking (load balancing, resizing)
- Code organization and modularity
"""