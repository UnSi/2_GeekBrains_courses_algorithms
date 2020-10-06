from collections import ChainMap

d_1 = {'a': 2, 'b': 4, 'c': 6}
d_2 = {'a': 10, 'b': 20, 'd': 40}

d_map = ChainMap(d_1, d_2)
print(d_map)
d_2['a'] = 20

print(d_map)

print(d_map['a'])
print(d_map['d'])


print('*' * 50)
x = d_map.new_child({'a': 111, 'b': 222, 'c': 333, 'd': 444})
print(x)

print(x.maps[0])
print(x.maps[-1])

print(x.parents)
print('*' * 50)

y = d_map.new_child()
print(y)
print(y['a'])
y['a'] = 1
print(y)

print(list(y))
print(list(y.values()))