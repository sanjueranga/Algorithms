# prims algorithm - adjecency list and binary heap
import heapq

# adjacency list for Prims Algorithm with Priority Queue
adj_list_graph = [
    [(1, 2), (3, 6)],
    [(0, 2), (2, 3), (3, 8), (4, 5)],
    [(1, 3), (4, 7)],
    [(0, 6), (1, 8), (4, 9)],
    [(1, 5), (2, 7), (3, 9)],
]


# Prims Algorithm with a Priority Queue
# Implemented with HeapQ
def prims_priority_q(graph, start):
    # establish the necessary data structures
    edges = []
    weights = []
    visited_vertices = [start]

    while len(visited_vertices) < len(graph):
        moves = []
        for x in visited_vertices:
            for node in graph[x]:
                if node[0] not in visited_vertices:
                    heapq.heappush(moves, (node[1], x, node[0]))
                    # get the next move based on the weight

                next_move = heapq.heappop(moves)
                print(f"next move: {next_move}")

        # add the next vertex, total weight, and append the edge
        visited_vertices.append(next_move[2])
        weights.append(next_move[0])
        edges.append((next_move[1], next_move[2]))
        return edges, weights


edges, weights = prims_priority_q(adj_list_graph, 0)
print("edges weights")
for edge, weight in zip(edges, weights):
    print(f"{edge} {weight}")
