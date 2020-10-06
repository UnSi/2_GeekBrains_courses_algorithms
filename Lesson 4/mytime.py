import timeit

x = 2 + 2
print(timeit.timeit('x = 2 + 2'))
print(timeit.timeit('x = sum(range(10))'))

# python -m timeit -n 100 -s "import mytime"