# CacheCraft
CacheCraft is a custom in-memory caching system designed to improve application performance by storing and retrieving data with low-latency access.
`This Project is fully inspired by Memcached`

## How to Use?
```
pip install CacheCraft
```
### Example 1 (General Set & Get)
```
>>> from cachecraft.cache import CacheCraft
>>> cache = CacheCraft()
>>> cache.set('key', 'value')
>>> cache.get('key')
'value'
```
### Example 2 (With Size and Default Time to live logic)
```
>>> cache = CacheCraft(max_size =100, default_ttl =2)
>>> cache.set('key', 'value')
>>> cache.get('key')
'value'
>>> import time; time.sleep(2)
>>> cache.get('key')
>>> 
```
### Example 3 (Least Recently Used LRU)
```
# Size is 3 so, if 4rth key will be added then
# oldest used will be removed
>>> from cachecraft.cache import CacheCraft
>>> cache = CacheCraft(max_size=3, default_ttl=30)
>>> cache.set('a', 1)
>>> cache.set('b', 2)
>>> cache.set('c', 3)
>>> cache.get('a')
1
>>> cache.get('c')
3
>>> cache.set('d', 4)  # Once 'd' will set 'b' will be removed 
>>> cache.get('b')     # due to LRU
>>> 
```
<img width="1440" alt="Screenshot 2024-10-03 at 9 02 31 AM" src="https://github.com/user-attachments/assets/833394e4-1e42-4e84-a36e-7f0d9071e110">


## Validating through Testcase
```
git clone git@github.com:Aditya-1998k/CacheCraft.git
pip install pytest
pytest tests/
```
<img width="1440" alt="Screenshot 2024-10-03 at 9 16 48 AM" src="https://github.com/user-attachments/assets/c6d68388-3f2f-4884-8b5c-3666b17c74df">


## Project Structure
```
CacheCraft/
├── cachecraft/
│   ├── __init__.py   # Package init file
│   ├── cache.py      # Core caching logic
├── tests/
│   ├── test_cache.py # pytest
├── setup.py          # Setup configuration for PyPI 
├── README.md         # Project description
└── LICENSE           # License file
```

## Features
```
1. Key-value store
2. Expiration : Optionally set TTl (time to live)
3. LRU Eviction Policy : Automatically evicts the least recently used entries
6. Customizable: Modify cache size, eviction policy etc.
```

## License
### This project is licensed under the MIT License. See the [LICENSE](https://github.com/Aditya-1998k/CacheCraft/blob/main/LICENSE) file for details.
