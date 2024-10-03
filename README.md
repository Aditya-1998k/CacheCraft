# CacheCraft
CacheCraft is a custom in-memory caching system designed to improve application performance by storing and retrieving data with low-latency access.
`This Project is fully inspired by Memcache and some code have references from memcached github repo.`

## Project Structure
```
CacheCraft/
├── cachecraft/
│   ├── __init__.py   # Package init file
│   ├── cache.py      # Core caching logic
├── tests/
│   ├── test_cache.py # pytest
├── setup.py          # Setup configuration for PyPI
|── Dockerfile        # Dockerfile  
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
