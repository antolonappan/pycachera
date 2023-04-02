# PyCachera
A powerful python decorator to cache functions

[![Tests](https://github.com/antolonappan/pycachera/actions/workflows/test.yml/badge.svg)](https://github.com/antolonappan/pycachera/actions/workflows/test.yml)
[![PyPI / GitHub](https://github.com/antolonappan/pycachera/actions/workflows/publish.yml/badge.svg)](https://github.com/antolonappan/pycachera/actions/workflows/publish.yml)
[![CodeQL](https://github.com/antolonappan/pycachera/actions/workflows/codeql.yml/badge.svg)](https://github.com/antolonappan/pycachera/actions/workflows/codeql.yml)
[![Docker](https://github.com/antolonappan/pycachera/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/antolonappan/pycachera/actions/workflows/docker-publish.yml)
[![wakatime](https://wakatime.com/badge/user/e4d61f54-a71a-4db6-81a9-edbb50ce497f/project/49c3495a-f7c4-416b-92b9-2f80ef1b43d2.svg)](https://wakatime.com/badge/user/e4d61f54-a71a-4db6-81a9-edbb50ce497f/project/49c3495a-f7c4-416b-92b9-2f80ef1b43d2)
[![Documentation Status](https://readthedocs.org/projects/pycachera/badge/?version=latest)](https://pycachera.readthedocs.io/en/latest/?badge=latest)

## Installation

In command line:

`pip install pycachera`

## Usage

Import the pycachera as:

```
from pycachera import cache
```

For caching a function
```
@cache()
def sum(a,b):
   return a+b
```

For caching a class attributes.

```
class Math:
   def __init__(self):
       pass
   
   @cache()
   def sum(a,b):
      return a + b  
```

For caching to a specific directory.

```
@cache(cachefolder='/home/user/scratch')
def sum(a,b):
   return a+b
```

For caching with a specific key

```
@cache(cachekey='This a custom cache')
def sum(a,b):
   return a+b
```

For printing the info

```
@cache(verbose=True)
def sum(a,b):
   return a+b
```

While debugging your script if you want to ignore the cached values you can recache
```
@cache(recache=True)
def sum(a,b):
   return a+b
```

When you use cache with a class attribute, and if you want to consider some attributes of that class for caching,
class Math:
   def __init__(self,c):
       self.c = c
   
   @cache(extrarg=['c'])
   def sum(a,b):
      return a + b  




## API

visit [pycachera.readthedocs.io](https://pycachera.readthedocs.io/en/latest/)
