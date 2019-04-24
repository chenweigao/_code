import sys
import heapq


def BuildGraph(shortcut_list, begin, end):
    points = set()

    for s in shortcut_list:
        points.add(s[0])
        points.add(s[1])
    points.add(begin)
    points.add(end)
    points = list(points)

    # print(points)

    begin_index = points.index(begin)
    end_index = points.index(end)
    graph = []
    size = len(points)

    # for i in range(size):
    for i in range(size):
        graph.append([0] * size)
        for j in range(size):
            graph[i][j] = abs(points[i] - points[j])

    for s in shortcut_list:
        _from = points.index(s[0])
        _to = points.index(s[1])
        _weight = s[2]
        graph[_from][_to] = _weight

    return (points, graph, begin_index, end_index)


# def floyd(graph, begin_index, end_index, depth):
#     if depth <= 0:
#         return graph[begin_index][end_index]
#     return min([floyd(graph, begin_index, i, depth - 1)
#                 + floyd(graph, i, end_index, depth - 1)
#                 for i in range(len(graph))])


# points, graph, bi, ei = BuildGraph([(0, 10, 1), (13, 8, 2)], 20, 7)


# print(floyd(graph, bi, ei, len(points) - 1))


def dijkstra(graph, src, goal):
    if graph is None:
        return None

    nodes = [i for i in range(len(graph))]
    visited = []
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance = {src: 0}
    for i in nodes:
        distance[i] = graph[src][i]

    k = src
    while nodes:
        mid_distance = float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v] + graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance
                    k = d
        distance[k] = mid_distance
        visited.append(k)
        nodes.remove(k)
        if k == goal:
            return distance[k]

    # return distance[goal]

# str_in = input()
# n, m = [int(_) for _ in str_in.split()]

# lines = []
# for line in sys.stdin:
#     list_new = line.split()

#     list_new = [int(_) for _ in list_new]
#     lines.append(list_new)
# shortcut_list = []
# for i in range(n):
#     shortcut_list.append(lines[i])
# datas = []
# for j in range(m):
#     datas.append(lines[j + n])

# for data in datas:
#     start = data[0]
#     end = data[1]
#     points, graph, bi, ei = BuildGraph(shortcut_list, start, end)

#     distance = dijkstra(graph, bi, ei)
#     print(distance)


points, graph, bi, ei = BuildGraph([(0, 10, 1), (13, 8, 2)], 20, 7)

distance = dijkstra(graph, bi, ei)
print(distance)


class Node:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost


def dijkstraHeap(graph, src, goal):
    if graph is None:
        return None
    pq = []
    visited = [0] * len(graph)
    heapq.heappush(pq, Node(src, 0))
    while len(pq) > 0:
        t = heapq.heappop(pq)
        if t.node == goal:
            return t.cost
        if visited[t.node]:
            continue
        visited[t.node] = True
        for i in range(len(graph)):
            if (graph[t.node][i] and not visited[i]):
                heapq.heappush(pq, Node(i, t.cost + graph[t.node][i]))
    return -1


distance1 = dijkstraHeap(graph, bi, ei)
print("heap result is:", distance1)
