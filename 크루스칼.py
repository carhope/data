MAX = 4

class GraphType:

    def __init__(self):

        self.n = MAX
        self.adj_mat = [[0 for _ in range(MAX)] for _ in range(MAX)]

def insert_edge(g, u, v, weight ): #각각 그래프, x,y, 값

    g.adj_mat[u][v] = weight #x,y
    g.adj_mat[v][u] = weight #y,x

def find(parent, x):

    if parent[x] == x:
        return x

    parent[x] = find(parent, parent[x])

    return parent[x]

def union(parent, a, b):

    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a

def kruskal(g):

    edges = []

    for i in range(g.n):

        for j in range(i + 1, g.n):

            if g.adj_mat[i][j] != 0:

                edges.append((g.adj_mat[i][j], i, j))

    edges.sort()

    parent = [i for i in range(g.n)]

    total_weight = 0
    selected_edges = 0

    print("Kruskal MST 간선")

    for weight, u, v in edges:

        if find(parent, u) != find(parent, v):

            union(parent, u, v)

            total_weight += weight
            selected_edges += 1

            print(f"{u} - {v} : {weight}")

        if selected_edges == g.n - 1:
            break

    print("총 가중치 :", total_weight)

g = GraphType()

insert_edge(g, 0, 1, 10)
insert_edge(g, 0, 2, 6)
insert_edge(g, 0, 3, 5)
insert_edge(g, 1, 3, 15)
insert_edge(g, 2, 3, 4)

kruskal(g)