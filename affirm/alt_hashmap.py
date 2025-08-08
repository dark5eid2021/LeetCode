# simplified version without resizing (for basic interviews)

class MyHashMapSimple:
    """
    Simplified HashMap without dynamic resizing
    Good for demonstrating core concepts without complexity
    """
    
    def __init__(self):
        self.bucket_count = 1000
        self.buckets = [[] for _ in range(self.bucket_count)]
    
    def _hash(self, key):
        return key % self.bucket_count
    
    def put(self, key, value):
        bucket = self.buckets[self._hash(key)]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))
    
    def get(self, key):
        bucket = self.buckets[self._hash(key)]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return -1
    
    def remove(self, key):
        bucket = self.buckets[self._hash(key)]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return

    

# Alternative: Open addressing with linear probing
class MyHashMapOpenAddressing:
    """
    HashMap using open addressing with linear probing
    
    Pros: Better cache performance, no extra memory for links
    Cons: More complex deletion, clustering issues
    """
    
    def __init__(self):
        self.capacity = 1000
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.deleted = [False] * self.capacity
    
    def _hash(self, key):
        return key % self.capacity
    
    def _find_slot(self, key):
        """Find slot for key using linear probing"""
        index = self._hash(key)
        
        while (self.keys[index] is not None and 
               self.keys[index] != key and 
               not self.deleted[index]):
            index = (index + 1) % self.capacity
        
        return index
    
    def put(self, key, value):
        if self.size >= self.capacity * 0.75:
            self._resize()
        
        index = self._find_slot(key)
        
        if self.keys[index] is None or self.deleted[index]:
            self.size += 1
        
        self.keys[index] = key
        self.values[index] = value
        self.deleted[index] = False
    
    def get(self, key):
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key and not self.deleted[index]:
                return self.values[index]
            index = (index + 1) % self.capacity
        
        return -1
    
    def remove(self, key):
        index = self._hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key and not self.deleted[index]:
                self.deleted[index] = True
                self.size -= 1
                return
            index = (index + 1) % self.capacity
    
    def _resize(self):
        # Resize implementation (complex, often skipped in interviews)
        pass


# Performance comparison helper
def compare_implementations():
    """
    Compare performance characteristics of different implementations
    """
    import time
    
    implementations = [
        ("Chaining", MyHashMapSimple()),
        ("Simple Chaining", MyHashMapSimple()),
    ]
    
    n = 10000
    
    for name, hashmap in implementations:
        start_time = time.time()
        
        # Insert
        for i in range(n):
            hashmap.put(i, i * 2)
        
        # Get
        for i in range(n):
            hashmap.get(i)
        
        # Remove half
        for i in range(0, n, 2):
            hashmap.remove(i)
        
        end_time = time.time()
        print(f"{name}: {end_time - start_time:.4f} seconds")