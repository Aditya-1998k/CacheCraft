from setuptools import setup, find_packages

setup(
    name='CacheCraft',  # Your package name
    version='0.1.2',
    description='A simple in-memory caching module like Memcached',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aditya Gupta',
    author_email='aditya98gupta@gmail.com',
    url='https://github.com/Aditya-1998k/CacheCraft',
    packages=find_packages(include=['cachecraft', 'cachecraft.*']),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
