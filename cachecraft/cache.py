import time
from threading import RLock
from collections import OrderedDict


class CacheCraft:
    def __init__(self, max_size=100, default_ttl=60):
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.cache = OrderedDict() # OrderDict to maintain LRU order
        self.lock = RLock()

    def set(self, key, value, ttl=None):
        """
        If the key already exists, remove it so we can re-insert
        it and mark it as recently used
        """
        with self.lock:
            if key in self.cache:
                del self.cache[key]
            elif len(self.cache) >= self.max_size:
                self.delete_oldest()
            expiration_time = time.time() + (ttl or self.default_ttl)
            self.cache[key] = (value, expiration_time)
    
    def get(self, key):
        with self.lock:
            if key in self.cache:
                value, expiration_time = self.cache[key]
                if expiration_time > time.time():
                    self.cache.move_to_end(key) # Mark it recently used
                    return value
                self.delete(key) # if expired delete it
            return None

    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
    
    def delete_oldest(self):
        with self.lock:
            if self.cache:
                # Remove the least used Record
                self.cache.popitem(last=False)
