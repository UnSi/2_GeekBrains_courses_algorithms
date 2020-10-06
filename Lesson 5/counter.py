from collections import Counter

a = Counter()
b = Counter('abrakadabra')
c = Counter({'red': 2, 'blue': 4})
d = Counter(cats=4, dogs=5)

print(a, b, c, d, sep='\n')
print(b['z'])
b['z'] = 0
print(b)

print(list(b.elements()))

print(b.most_common(3))

g = Counter(a=4, b=6, c=-2, d=0)
f = Counter(a=1, b=2, c=3, d=-2)

g.subtract(f)
print(g)

g.clear()
print(g)

print('*' * 50)

x = Counter(a=3, b=1)
y = Counter(a=2, b=2)

print(x+y)
print(x-y)
print(x|y)
print(x&y)

print('*' * 50)
z = Counter(a=2, b= -4)

print(+z)
print(-z)