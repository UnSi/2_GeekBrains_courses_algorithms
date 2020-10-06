def test_fib(func):
    lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def fib_dict(n):
    fib_d = {0:0, 1:1}

    def _fib_dict(n):
        if n in fib_d:
            return fib_d[n]

        fib_d[n] = _fib_dict(n-1) + _fib_dict(n-2)
        return fib_d[n]
    return _fib_dict(n)


def fib_list(n):
    fib_l = [None] * 1000
    fib_l[:2] = [0, 1]

    def _fib_list(n):
        if fib_l[n] is None:
            fib_l[n] = _fib_list(n - 1) + _fib_list(n - 2)
        return fib_l[n]

    return _fib_list(n)

def fib_loop(n):

    if n < 2:
        return n

    first, second = 0, 1
    for i in range(2, n+1):
        first, second = second, first+second

    return second


test_fib(fib_loop)

# python -m timeit -n 1000 -s "import fib2" "fib2.fib_dict(10)"

# "fib2.fib_dict(10)"
# 1000 loops, best of 5: 7.41 usec per loop

# "fib2.fib_dict(15)"
# 1000 loops, best of 5: 11 usec per loop