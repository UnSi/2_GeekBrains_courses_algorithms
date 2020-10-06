# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
from random import randint, choice
from random import randrange

n = int(input("Введите кол-во врешин"))

'''
Триллион лет писал генератор случайных графов. Вроде даже нормально генерирует графы с путями из нулевого элемента к остальным, 
в чём не уверен. И потом наткнулся на тему, где сакцентировано внимание на том, что он не обязательно должен быть случайным.
Оставил закомментированным на память потомкам. Покойся с миром. Если понадобится - когда-нибудь доработаю.

def get_graph(n):
    graph = [[] for _ in range(n)]
    
    # случайно генерируем граф без петель в виде списка смежности
    for i in range(n):
        for j in range(n):
            if i != j and randint(0, 1):
                graph[i].append(j)

    # n = 5
    # graph = [[4], [2], [], [1, 2, 4], [0, 2]]
    # # graph = [[4],[4],[0, 1, 4],[0, 2, 4],[3]]
    # # graph = [[1],[0],[1, 4],[1, 4],[1, 3]]
    # # n = 6
    # # graph = [[1, 2],[2, 3],[3, 1],[],[5],[4]]
    # print('*' * 50)
    # print(*graph, sep='\n')
    # print('*' * 50)
    
    # для хранения элементов, пути из которых уже исследованы
    is_used = [False for _ in range(n)]

    def _test_graph(graph, line=0):

        # если исходящих связей связей нет, добавляем случайную - упрощает жизнь
        if not graph[line]:
            spam = [i for i in range(n)]
            spam.remove(line)
            spam = choice(spam)
            graph[line].append(spam)
           
        # ищем неисследованные вершины в связях текущей    
        for item in graph[line]:
            if not is_used[item]:
                is_used[line] = is_used[item] = True
                # рекурсивно запускаем такой же поиск внутри этой вершины:
                _test_graph(graph, item)

        return

    _test_graph(graph)

    # для отладки, проверка, всем ли элементам найдена связь
    # print(is_used)
    last_true = -1

    for i in range(len(is_used)):
        if is_used[i]:
            last_true = i
        if not is_used[i]:
             # если связи с этим элементом нет, добавляем какому-нибудь уже существующуему ребро с этим элементом.
             
            if last_true >= 0:
                graph[last_true].append(i)
                
            else:
                spam = [j for j in range(n)]
                spam.remove(i)
                spam = choice(spam)
                graph[spam].append(i)
                
            is_used = [False for _ in range(n)]
            _test_graph(graph)
            # print(is_used)

    if False in is_used:
        graph = get_graph(n)

    return graph
'''

# граф в данном генераторе - элементарное кольцо c несколькими случайными ветками, но алгоритм работает на графах любой сложности
# (до 1000 вызовов функции - при необходимости можно исправить)

# для теста можно раскоментировать функцию выше - она генерирует слабо-связный граф, в котором гарантировано будет путь
# в любую точку из нулевой. Тогда функцию ниже - закомментирвать или переименовать.

# если надо поискать пути из другой вершины, в вызове dfs(g) 2м параметром указать вершину. Можно вообще циклом прогнать.


def get_graph(n):
    graph = [[] for _ in range(n)]

    for line in range(len(graph)-1):
        graph[line].append(line+1)

        for j in range(n):
            if j not in (line, line+1) and randint(0, 1):
                graph[line].append(j)
        graph[line].sort()

    graph[-1].append(0)
    for j in range(1, n - 1):
        if randint(0, 1):
            graph[-1].append(j)

    return graph


# вариант преподавателя:
# def get_graph_teacher(n, percent=1.0):
#     assert 0 < percent <= 1, "Неверный диапазон"
#
#     graph = {}
#
#     for i in range(n):
#         graph[i] = set()
#
#         count_edge = randrange(1, int(n*percent))
#         while len(graph[i]) < count_edge:
#             edge = randrange(0, n)
#             if edge != i:
#                 graph[i].add(edge)
#
#     return graph


is_visited = [False for _ in range(n)]


def dfs(graph, start=0):
    is_visited[start] = True
    for item in graph[start]:
        if not is_visited[item]:
            dfs(graph, item)
    print('Нашёл', start)
    return


g = get_graph(n)

print(g, sep='\n')
print('*' * 50)
dfs(g)



