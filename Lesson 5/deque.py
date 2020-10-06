# deque - очередь

from collections import deque

a = deque()
b = deque('abcdef')
c = deque([1, 2, 3, 4, 5])
print(a, b, c, sep='\n')

b = deque('abcdef', maxlen=3)
c = deque([1, 2, 3, 4, 5], maxlen=4)
c.clear()
print(b, c, sep='\n')

print('*' * 50)
d = deque([i for i in range(5)], maxlen=7)
d.append(5)
d.appendleft(6)
print(d)
print('*' * 50)
d.extend([7, 8, 9])
print(d)
d.extendleft([10, 11, 12])
print(d)
print('*' * 50)

f = deque([i for i in range(5)], maxlen=7)
x = f.pop()
y = f.popleft()

print(f, x, y, sep='\n')

print('*' * 50)
g = deque([i for i in range(5)], maxlen=7)
print(g.count(2))
print(g.index(3))
g.insert(2, 6)
print(g)

g.reverse()
print(g)

g.rotate(3)
print(g)