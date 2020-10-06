import hashlib


print(hashlib.sha1(b'Hello World!').hexdigest())

print(hashlib.sha1(b'secretword' + b'Hello World.').hexdigest())

s = hashlib.sha1(b'Hello World!').hexdigest()

print(s.encode('utf-8'))

print(hashlib.sha1(b'secretword' + bytes(s.encode('utf-8'))).hexdigest())

dict = {'a': 5}
print(dict)
print(dict.popitem())

import os

var = 'sd'
print(var.encode('utf-8'))


print([] or {} or 0)