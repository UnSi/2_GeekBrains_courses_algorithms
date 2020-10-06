from collections import namedtuple, OrderedDict



hero1 = ('Aaz', 'Izverg', 100, 0.0, 250)


class Person:
    def __init__(self, name, race, health, mana, strength):
        self.name, self.race, self.health, self.mana, self.strength = name, race, health, mana, strength


hero2 = Person('Aaz', 'Izverg', 100, 0.0, 250)

print(hero2.mana)

New_Person = namedtuple('New_Person', 'name, race, health, mana, strength')
hero3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero3.race)


stats = ['name', '3race', 'health', '_mana', 'strength']
New_Person2 = namedtuple('New_Person2', stats, rename=True)
hero4 = New_Person2('Aaz', 'Izverg', 100, 0.0, 250)
print(hero4)


print('*' * 50)
Point = namedtuple('Point', 'x, y, z')
p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]

p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)
print(type(d2))

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)
print('*' * 50)

New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0, 0])
p4 = New_Point(2)
print(p4)

print(p4._field_defaults)

dct = {'x': 10, 'y': 20, 'z':30}
p5 = New_Point(**dct)
print(p5)