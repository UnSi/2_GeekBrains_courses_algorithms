from collections import OrderedDict

a = {'cat': 5, 'dog': 2, 'mouse': 4}
new_a = OrderedDict(sorted(a.items(), key=lambda x: x[0]))

new_a.move_to_end('mouse')
print(new_a)

new_a.move_to_end('mouse', last=False)
print(new_a)

new_a.popitem(last=False)
print(new_a)

new_a['cow'] = 1
print(new_a)

print('*' * 50)
new_c = OrderedDict(sorted(a.items(), key=lambda x: len(x[0])))
for key in reversed(new_c):
    print(key, new_c[key])