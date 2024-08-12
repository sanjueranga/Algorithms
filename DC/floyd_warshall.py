def floyd_warshall(graph):
    n = len(graph)
    dist = [graph[i][:] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def all_pairs_shortest_path(pi, i, j):
    if i == j:
        print(i)

    else:
        if pi[i][j] == None:
            print("No path from ", i, " to ", j, " exists")
        else:
            all_pairs_shortest_path(pi, i, pi[i][j])
            print(j)
