# Copy from https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/

MAXINT = float('inf')


def min_dist(dist, queue):
    minimum = MAXINT
    min_index = -1

    for i in range(len(dist)):
        if dist[i] < minimum and i in queue:
            minimum = dist[i]
            min_index = i
    return min_index


def print_path(parent, j):
    if parent[j] == -1:
        print(j, end=' ')
        return
    print_path(parent, parent[j])
    print(j, end=' ')


def get_solution(dist, parent, src):
    print("Vertex \t\t\t Path")
    for i in range(1, len(dist)):
        print("%d --> %d \t\t" % (src, i), end='')
        print_path(parent, i)


def dijkstra(mat, src, alpha=0.5):
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

    # Variable initialization
    row = len(graph)
    col = len(graph[0])
    dist = [MAXINT] * row
    dist[src] = 0
    parent = [-1] * row

    # Add all vertices in queue
    queue = []
    for i in range(row):
        queue.append(i)

    # Find shortest path for all vertices
    while queue:
        u = min_dist(dist, queue)
        queue.remove(u)

        for i in range(col):
            if graph[u][i] and i in queue:
                if dist[u] + graph[u][i] ** alpha < dist[i]:
                    dist[i] = dist[u] + graph[u][i] ** alpha
                    parent[i] = u

    get_solution(dist, parent, src)


# # Test part
# adj_mat = [
#     [0,0.3,0,0,0,0,0.1,2,0,0,0,0,0,0,0,0,0,0,0],    # RAND
#     [0.3,0,0.7,0,0,0.3,0,0,0,0,0,0,0,0,0,0,0,0,0],  # UCSB
#     [0,0.7,0,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0],    # SU
#     [0,0,0.1,0,0.1,0,0,0.1,0,0,0,0,0,0,0,0,0,0,0],  # UCB
#     [0,0,0,0.1,0,0.1,0,0,0,0,0,0,0,0,8,0,0,0,0],    # SRI
#     [0,0.3,0,0,1,0,0.1,0,0,0,0,0,0,0,0,0,0,0,0],    # UCLA
#     [0.1,0,0,0,0,0.1,0,0,5,0,0,0,0,0,0,0,0,0,0],    # SDC
#     [2,0,0,0.1,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0],      # UTAH
#     [0,0,0,0,0,0,5,0,0,0.4,0,1.8,0,0,0,0,0,0,0],    # WU
#     [0,0,0,0,0,0,0,4,0.4,0,1,0,0,0,0,0,0,0,0],      # ILL
#     [0,0,0,0,0,0,0,0,0,1,0,0,0,1.5,0,0,0,0,1.8],    # MICH
#     [0,0,0,0,0,0,0,0,1.8,0,0,0,0.5,0,0,0,1.4,0,0],  # CMU
#     [0,0,0,0,0,0,0,0,0,0,0,0.5,0,0.6,0,0,0,0,0],    # ARPA
#     [0,0,0,0,0,0,0,0,0,0,1.5,0,0.6,0,0,0.6,0,0,0],  # BTL
#     [0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0.1,0,0,0.3],    # HARV
#     [0,0,0,0,0,0,0,0,0,0,0,0,0,0.6,0.1,0,0.1,0,0],  # LL
#     [0,0,0,0,0,0,0,0,0,0,0,1.4,0,0,0,0.1,0,0.1,0],  # BBN
#     [0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0,0.3],    # MAC
#     [0,0,0,0,0,0,0,0,0,0,1.8,0,0,0,0.3,0,0,0.3,0]   # DART
# ]
#
# dijkstra(adj_mat, 0)
