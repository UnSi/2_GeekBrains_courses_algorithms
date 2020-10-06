# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
from collections import namedtuple


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 7, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    vert_info = namedtuple("vert_info", "cost, way")
    first = start

    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    vi = {}
    for i in range(length):
        way = []
        j = i
        if parent[j] != -1:
            while j != first:
                way.insert(0, parent[j])
                j = parent[j]
        if way or cost[i] == 0:
            way.append(i)
        else:
            way = ['not found']
        vi[i] = vert_info(cost[i], way)

    return vi


s = int(input('От какой вершини идти: '))
vi = dijkstra(g, s)

for k, v in vi.items():
    print(f"к вершине {k}, стоимость: {v.cost}, путь:", *v.way)