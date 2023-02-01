# subscriptlib

Python library for automatic text conversion to subscript

- A simple easy to use set of functions
- Lightweight and no external dependencies

## Usage

```shell
$ pip install subscriptlib
```

```python
from subscriptlib import subscript

print(f'H{subscript(2)}O{subscript(2)}')
```
Result:
```
H₂O₂
```

Also works the same way with the superscript
```python
from subscriptlib import superscript

print(f'H{superscript(2)}O{superscript(2)}')
```
Result:
```
H²O²
```

## Meta
Lev Zharikov - lev_zharikov@outlook.com

Distributed under MIT License, see LICENSE for more information

https://github.com/Leozaur1808/subscriptlib
