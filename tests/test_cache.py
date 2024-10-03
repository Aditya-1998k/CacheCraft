import time
from cachecraft.cache import CacheCraft

def test_set_get():
    cache = CacheCraft()
    cache.set('foo', 'bar')
    assert cache.get('foo') == 'bar'

def test_expiration():
    cache = CacheCraft(default_ttl=1)
    cache.set('foo', 'bar')
    time.sleep(2)
    assert cache.get('foo') is None
