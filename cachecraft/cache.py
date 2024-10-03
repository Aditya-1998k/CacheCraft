import time
from threading import RLock


class CacheCraft:
    def __init__(self, max_size=100, default_ttl=60):
        self.max_size = max_size
        self.default_ttl = default_ttl
        self.cache = {}
        self.lock = RLock()

    def set(self, key, value, ttl=None):
        with self.lock:
            if len(self.cache) >= self.max_size:
                self.delete_oldest()
            expiration_time = time.time() + (ttl or self.default_ttl)
            self.cache[key] = (value, expiration_time)
    
    def get(self, key):
        with self.lock:
            if key in self.cache:
                value, expiration_time = self.cache[key]
                if expiration_time > time.time():
                    return value
                self.delete(key)

    def delete(self, key):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
    
    def delete_oldest(self):
        with self.lock:
            oldest_key = min(self.cache, key=lambda k: self.cache[k][1])
            del self.cache[oldest_key]
