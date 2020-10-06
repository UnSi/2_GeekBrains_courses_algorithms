import cProfile


def get_len(array):
    return len(array)


def get_sum(array):
    s = 0
    for i in array:
        s+=1
    return s


def main():
    lst = [i for i in range(100000000)]
    a = get_len(lst)
    b = get_sum(lst)


cProfile.run('main()')