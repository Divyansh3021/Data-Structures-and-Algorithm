class HashMap:
    def __init__(self, size = 16):
        self.size = size
        self.buckets = [ []  for i in range(self.size)]

    def _hashing_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hashed_key = self._hashing_function(key)
        bucket = self.buckets[hashed_key]

        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
        
        bucket.append((key, value))

    def get_value(self, key):
        hashed_key = self._hashing_function(key)
        bucket = self.buckets[hashed_key]

        for (existing_key, existing_value) in bucket:
            if existing_key == key:
                return existing_value
        
        return -1

    def delete(self,key):
        hashed_key = self._hashing_function(key)
        bucket = self.buckets[hashed_key]

        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]

        return -1

hashmap = HashMap()
hashmap.insert(2, "Divyansh")
hashmap.insert(1, None)
print(hashmap.get_value(1))
print(hashmap.get_value(2))
hashmap.insert(1, "Divyansh")
print(hashmap.get_value(1))
hashmap.delete(2)
print(hashmap.get_value(2))