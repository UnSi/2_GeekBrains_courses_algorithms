# 2. Закодируйте любую строку по алгоритму Хаффмана.

import collections


class MyNode:
    level = 0

    def __init__(self, left=(None, 0), right=(None, 0)):
        self.left = left[0]
        self.right = right[0]
        self.weight = left[1] + right[1]
        MyNode.level += 1

    def __str__(self):
        tab = '   ' * (MyNode.level - len(self))
        return f'\n{tab}[Left: _{self.left}_\n{tab}Right: _{self.right}_]'

    def __len__(self):
        return len(self.left) + len(self.right)


def get_tree(s: str):
    counter = collections.Counter(s).most_common()

    if len(counter) == 1:
        el = MyNode(counter[0])
        return el

    deq = collections.deque(reversed(counter))
    # print(deq)

    while len(deq) > 1:
        el = MyNode(deq.popleft(), deq.popleft())

        if not len(deq):
            deq.append((el, el.weight))
            break
        for i, item in enumerate(deq):

            if el.weight <= item[1]:
                deq.insert(i, (el, el.weight))
                break

            if item == deq[-1]:
                deq.append((el, el.weight))
                break

    return deq[0][0]


def get_code_dict(some_tree):
    vars = {}

    def _code(some_tree, sym_code=[]):
        if type(some_tree) == str:
            vars[some_tree] = ''.join(sym_code)
            return

        left, right = some_tree.left, some_tree.right
        if left:
            sym_code.append('0')
            _code(left, sym_code)
            sym_code.pop()

        if right:
            sym_code.append('1')
            _code(right, sym_code)
            sym_code.pop()

        return

    _code(some_tree)
    return vars


def encode_haffman(s):
    assert len(s), 'Строка должна быть не пустая'

    tree = get_tree(s)
    # print(tree)
    code_dict = get_code_dict(tree)
    result = ''

    for letter in s:
        result += code_dict[letter]
        # для удобства можно добавить пробел
        # result += " "

    return code_dict, result


def decode_haffman(s, key_dict):
    result = ''
    key_dict = {v: k for k, v in key_dict.items()}
    key = ''
    for letter in s:
        # если добавлен пробел для читаемости - раскомментировать
        # if letter == " ":
        #     continue

        key += letter
        if key in key_dict:
            result += key_dict[key]
            key = ''

    return result


s_1 = input("Введите строку:")
# s_1 = 'beep boop beer!'
res_tuple = encode_haffman(s_1)

print(f'Обозначения: {res_tuple[0]}\n Закодированная строка : {res_tuple[1]}')

s_2 = decode_haffman(res_tuple[1], res_tuple[0])
print(f'Декодированная строка: {s_2}')
