# Nice video about Edmonds Karp Algorithm for Max-Flow: https://www.youtube.com/watch?v=SqGeM3FYkfo

from collections import deque


INF = float("inf")


class Graph:
    def __init__(self, entrances, exits, path):
        self.graph = [list(row) for row in path]
        self.nodes_number = len(self.graph)
        self.max_flow = None

        self.entrance = self.nodes_number
        self.exit = self.nodes_number + 1

        for row in xrange(self.nodes_number):
            self.graph[row].append(0)
            self.graph[row].append(INF if row in exits else 0)

        self.nodes_number += 2

        self.graph.append([(INF if x in entrances else 0) for x in xrange(self.nodes_number)])
        self.graph.append([0] * self.nodes_number)

    def bfs(self):
        visited = set()
        deq = deque()
        deq.append((self.entrance, [self.entrance]))

        while len(deq) > 0:
            current, path = deq.popleft()
            if current == self.exit:
                return path

            for i in xrange(self.nodes_number):
                if i not in visited and self.graph[current][i] > 0:
                    visited.add(i)
                    new_path = list(path)
                    new_path.append(i)
                    deq.append((i, new_path))

        return None

    def get_max_flow(self):
        if self.max_flow is None:
            max_flow = 0

            while True:
                shortest_path = self.bfs()

                if shortest_path is None:
                    break

                flow = INF
                for i in xrange(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    flow = min(flow, self.graph[node_from][node_to])

                for i in xrange(1, len(shortest_path)):
                    node_from = shortest_path[i - 1]
                    node_to = shortest_path[i]
                    self.graph[node_from][node_to] -= flow
                    self.graph[node_to][node_from] += flow

                max_flow += flow

            self.max_flow = max_flow

        return self.max_flow


def answer(entrances, exits, path):
    g = Graph(entrances, exits, path)
    return g.get_max_flow()

# SPOJ driver
#
# N, M = [int(x) for x in raw_input().split()]
# path = []
# for n in xrange(N):
#     path.append([0] * N)
#
# for e in xrange(M):
#     f, t, v = [int(x) for x in raw_input().split()]
#     f, t = f - 1, t - 1
#     f, t = min(f, t), max(f, t)
#
#     if path[t][f] > 0:
#         path[t][f] += v
#     else:
#         path[f][t] += v
#
# print(answer([0], [N - 1], path))


# http://www.cs.ust.hk/mjg_lib/Classes/COMP572_Fall07/Project/maxflow_test.txt
#
# T = int(raw_input())
#
# for t in xrange(T):
#     nodes_number = int(raw_input())
#     entrances = [0]
#     exits = [nodes_number - 1]
#     path = []
#     for i in xrange(nodes_number):
#         path.append([int(x) for x in raw_input().split()])
#
#     #print("entrances, exits, path: {}, {}, {}".format(entrances, exits, path))
#     answer_in = int(raw_input())
#     answer_my = answer(entrances, exits, path)
#     print("answer_in, answer_my, is_success: {}, {}, {}".format(answer_in, answer_my, answer_in == answer_my))
#
#



T = int(raw_input())

for t in xrange(T):
    entrances = [int(x) for x in raw_input().split()]
    exits = [int(x) for x in raw_input().split()]
    path_raw = [int(x) for x in raw_input().split()]
    path = []
    nodes_number = int(len(path_raw) ** 0.5)
    for i in xrange(nodes_number):
        path.append([])
        for j in xrange(nodes_number):
            path[i].append(path_raw[i*nodes_number + j])
    print("entrances, exits, path: {}, {}, {}".format(entrances, exits, path))
    answer_in = int(raw_input())
    answer_my = answer(entrances, exits, path)
    print("answer_in, answer_my, is_success: {}, {}, {}".format(answer_in, answer_my, answer_in == answer_my))





# entrances = [0]
# exits = [49]
# path_raw = [randint(0, 10) * randint(0, 1) for i in range(50 * 50)]
# path = []
# nodes_number = int(len(path_raw) ** 0.5)
# for i in xrange(nodes_number):
#     path.append([])
#     for j in xrange(nodes_number):
#         path[i].append(path_raw[i*nodes_number + j])
# print("entrances, exits, path: {}, {}, {}".format(entrances, exits, path))
# answer_in = -1
# answer_my = answer(entrances, exits, path)
# print("answer_in, answer_my, is_success: {}, {}, {}".format(answer_in, answer_my, answer_in == answer_my))
