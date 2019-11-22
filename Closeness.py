MAXINT = float('inf')


def min_dist(graph, dist, shortest_path_list):
    min_dist = MAXINT
    min_index = 0

    for v in range(len(graph)):
        if dist[v] < min_dist and shortest_path_list[v] is False:
            min_dist = dist[v]
            min_index = v

    return min_index


def dijkstra(mat, src, alpha=0.5):
    """
    :param mat: A 2*2 nested list (The adjacent matrix)
    :param src: the index of the source node
    :param alpha: weighted parameter
    :return:
    """
    # Do a convert of the original adjacent matrix
    graph = []
    for i in range(len(mat)):
        row = mat[i]
        new_row = []
        for j in row:
            if j == 0:
                new_row.append(0)
            else:
                new_row.append(1 / j)
        graph.append(new_row)

    dist = [MAXINT] * len(graph)
    dist[src] = 0
    shortest_path_list = [False] * len(graph)

    for i in range(len(graph)):
        u = min_dist(graph, dist, shortest_path_list)
        shortest_path_list[u] = True

        for v in range(len(graph)):
            if graph[u][v] > 0 \
                    and shortest_path_list[v] is False \
                    and dist[v] > dist[u] + graph[u][v] ** alpha:
                dist[v] = dist[u] + graph[u][v] ** alpha

    return sum(dist)