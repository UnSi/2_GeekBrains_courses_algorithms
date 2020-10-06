"""Закодируйте любую строку по алгоритму Хаффмана."""

from queue import PriorityQueue


class Node:

    def __init__(self, data, left=None, right=None, code=None):
        self.data = data
        self.left = left
        self.right = right
        self.code = code

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return False


def build_tree(pq):

    def add_code(node, code=''):
        node.code = code
        if node.right is not None:
            add_code(node.right, code + '1')
        if node.left is not None:
            add_code(node.left, code + '0')

    while pq.qsize() > 1:
        el1 = pq.get()
        el2 = pq.get()
        n = Node(data='')
        if isinstance(el1[1], Node):
            n.left = el1[1]
        else:
            n.left = Node(data=el1[1])
        if isinstance(el2[1], Node):
            n.right = el2[1]
        else:
            n.right = Node(data=el2[1])
        pq.put((el1[0] + el2[0], n))
    root = pq.get()[1]
    add_code(root)
    return root


def get_enc_dict(node, d=None):
    if d is None:
        d = dict()
    if node.data != '':
        d[node.data] = node.code
    if node.left is not None:
        get_enc_dict(node.left, d)
    if node.right is not None:
        get_enc_dict(node.right, d)
    return d


def huffman(message):
    pq = PriorityQueue()
    spam = set()

    for el in message:
        count = 0
        if el not in spam:
            for i in message:
                if i == el:
                    count += 1
            spam.add(el)
            pq.put((count, el))

    root = build_tree(pq)
    enc_dict = get_enc_dict(root)
    enc_message = ''
    for c in message:
        enc_message = f'{enc_message}{enc_dict[c]}'
    return enc_message


message = input('Введите сообщение: ')
print(f'Сообщение "{message}" кодируется в {huffman(message)}')






