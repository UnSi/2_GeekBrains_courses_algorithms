from collections import namedtuple

# списки смежности

graph = []

graph.append([1, 2])
graph.append([0, 2, 3])
graph.append([0, 1])
graph.append([1])

print(*graph, sep='\n')

# словарь множеств

graph_2 = {
    0: {1, 2},
    1: {0, 2, 3},
    2: {0, 1},
    3: {1}
}

print(graph_2)

if 3 in graph_2[1]:
    print(True)


# взвешенный граф
Vertex = namedtuple('Vertex', ['vertex', 'edge'])
graph_3 = []
graph_3.append([Vertex(1,2), Vertex(2,3)])
graph_3.append([Vertex(0,2), Vertex(2,2), Vertex(3,1)])
graph_3.append([Vertex(0,3), Vertex(1,2)])
graph_3.append([Vertex(1,1)])

print(*graph_3, sep='\n')

for v in graph_3[1]:
    if v.vertex == 3:
        print(True)



# список ребер

graph_4 = [(0, 1), (0, 2), (1, 2), (2, 1), (1, 3)]

print(*graph_4, sep='\n')

