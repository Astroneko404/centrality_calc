# Borrowed from here: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

        # A utility function to print the constructed MST stored in parent[]

    def printMST(self, parent):
        print("Edge \tWeight")

        for i in range(self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        MIN = float('inf')

        for v in range(self.V):
            if key[v] < MIN and not mstSet[v]:
                MIN = key[v]
                min_index = v

        return min_index

        # Function to construct and print MST for a graph

    # represented using adjacency matrix representation
    def primMST(self, src):

        # Key values used to pick minimum weight edge in cut
        key = [float('inf')] * self.V
        parent = [None] * self.V
        mstSet = [False] * self.V

        key[src] = 0
        parent[src] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minKey(key, mstSet)

            # Put the minimum distance vertex in
            # the shortest path tree
            mstSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                # graph[u][v] is non zero only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] is smaller than key[v]
                if 0 < self.graph[u][v] < key[v] \
                        and mstSet[v] == False:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)


adj_mat = [
    [0,0.3,0,0,0,0,0.1,2,0,0,0,0,0,0,0,0,0,0,0],    # RAND
    [0.3,0,0.7,0,0,0.3,0,0,0,0,0,0,0,0,0,0,0,0,0],  # UCSB
    [0,0.7,0,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,8,0],    # SU
    [0,0,0.1,0,0.1,0,0,0.1,0,0,0,0,0,0,0,0,0,0,0],  # UCB
    [0,0,0,0.1,0,1,0,0,0,0,0,0,0,0,8,0,0,0,0],    # SRI
    [0,0.3,0,0,1,0,0.1,0,0,0,0,0,0,0,0,0,0,0,0],    # UCLA
    [0.1,0,0,0,0,0.1,0,0,5,0,0,0,0,0,0,0,0,0,0],    # SDC
    [2,0,0,0.1,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0],      # UTAH
    [0,0,0,0,0,0,5,0,0,0.4,0,1.8,0,0,0,0,0,0,0],    # WU
    [0,0,0,0,0,0,0,4,0.4,0,1,0,0,0,0,0,0,0,0],      # ILL
    [0,0,0,0,0,0,0,0,0,1,0,0,0,1.5,0,0,0,0,1.8],    # MICH
    [0,0,0,0,0,0,0,0,1.8,0,0,0,0.5,0,0,0,1.4,0,0],  # CMU
    [0,0,0,0,0,0,0,0,0,0,0,0.5,0,0.6,0,0,0,0,0],    # ARPA
    [0,0,0,0,0,0,0,0,0,0,1.5,0,0.6,0,0,0.6,0,0,0],  # BTL
    [0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0.1,0,0,0.3],    # HARV
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0.6,0.1,0,0.1,0,0],  # LL
    [0,0,0,0,0,0,0,0,0,0,0,1.4,0,0,0,0.1,0,0.1,0],  # BBN
    [0,0,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0.1,0,0.3],    # MAC
    [0,0,0,0,0,0,0,0,0,0,1.8,0,0,0,0.3,0,0,0.3,0]   # DART
]
g = Graph(19)
g.graph = adj_mat

g.primMST(0)

# Contributed by Divyanshu Mehta
