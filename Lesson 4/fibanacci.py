import cProfile
import functools


def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')

@functools.lru_cache()
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n - 2)
    # return fib(n-1)

# test_fib(fib)

# cProfile.run('fib(15)')
# 1976 function calls (4 primitive calls) in 0.001 seconds
# 1973/1    0.001    0.000    0.001    0.001 fibanacci.py:12(fib)

# cProfile.run('fib(20)')
# 21894 function calls (4 primitive calls) in 0.007 seconds
# 21891/1    0.007    0.000    0.007    0.007 fibanacci.py:12(fib)



# python -m timeit -n 1000 -s "import fibanacci" "fibanacci.fib(10)"
# wo functools
'''
"fibanacci.fib(10)"
1000 loops, best of 5: 36.9 usec per loop

"fibanacci.fib(15)"
1000 loops, best of 5: 404 usec per loop

"fibanacci.fib(20)"
1000 loops, best of 5: 4.52 msec per loop

"fibanacci.fib(25)"
1000 loops, best of 5: 50.3 msec per loop
'''
#with functools
"""
 "fibanacci.fib(10)"
1000 loops, best of 5: 141 nsec per loop

"fibanacci.fib(15)"
1000 loops, best of 5: 142 nsec per loop

"fibanacci.fib(20)"
1000 loops, best of 5: 135 nsec per loop

 "fibanacci.fib(25)"
1000 loops, best of 5: 139 nsec per loop

"""