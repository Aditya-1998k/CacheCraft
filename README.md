# CacheCraft
CacheCraft is a custom in-memory caching system designed to improve application performance by storing and retrieving data with low-latency access.
`This Project is fully inspired by Memcache and some code have references from memcached github repo.`

## How to Use?
```
pip install CacheCraft
>>> from cachecraft.cache import CacheCraft
>>> cache = CacheCraft()
>>> cache.set('key', 'value')
>>> cache.get('key')
'value'
```
<img width="1440" alt="Screenshot 2024-10-03 at 9 02 31 AM" src="https://github.com/user-attachments/assets/833394e4-1e42-4e84-a36e-7f0d9071e110">


## Validating through Testcase
```
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
3. LRU Eviction Policy : Automatically evicts the least recently used entries (Try to Implement later of the Project)
4. Containerize services
5. HTTP API : Access through simple HTTP requests
6. Customizable: Modify cache size, eviction policy etc.
```

## License
### This project is licensed under the MIT License. See the [LICENSE](https://github.com/Aditya-1998k/CacheCraft/blob/main/LICENSE) file for details.
