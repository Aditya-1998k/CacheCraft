import time
import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from cachecraft.cache import CacheCraft

@pytest.fixture
def cache():
    """Fixture to create a CacheCraft instance for testing."""
    return CacheCraft(max_size=5, default_ttl=2)

def test_set_get(cache):
    """Test setting and getting a value in the cache."""
    cache.set('foo', 'bar')
    assert cache.get('foo') == 'bar'

def test_expiration(cache):
    """Test that a cache entry expires after its TTL."""
    cache.set('baz', 'qux', ttl=1)  # Set with a TTL of 1 second
    time.sleep(1.5)  # Wait for expiration
    assert cache.get('baz') is None  # Should be expired

def test_delete(cache):
    """Test deleting a cache entry."""
    cache.set('foo', 'bar')
    cache.delete('foo')
    assert cache.get('foo') is None  # Should be deleted

def test_cache_limit(cache):
    """Test that the cache does not exceed its maximum size."""
    for i in range(6):
        cache.set(f'key_{i}', f'value_{i}')  # This will add 6 items
    assert cache.get('key_0') is None  # The oldest item should be removed
    assert cache.get('key_1') is not None  # The next item should still exist
