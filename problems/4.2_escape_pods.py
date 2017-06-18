"""
Escape Pods
===========

You've blown up the LAMBCHOP doomsday device and broken the bunnies out of Lambda's prison - and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time.

Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function answer(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

For example, if you have:
entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

Then in each time step, the following might happen:
0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.  (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final answer remains the same.)

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) entrances = [0]
    (int list) exits = [3]
    (int) path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
Output:
    (int) 6

Inputs:
    (int list) entrances = [0, 1]
    (int list) exits = [4, 5]
    (int) path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Output:
    (int) 16


Time to solve: 360 hours.
"""

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
