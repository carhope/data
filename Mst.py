MAX = 4
INF = 9999

class GraphType:
    def __init__(self):
        self.n = MAX
        self.adj_mat = [[0 for _ in range(MAX)] for _ in range(MAX)]

def insert_edge(g, u, v, weight):

    g.adj_mat[u][v] = weight
    g.adj_mat[v][u] = weight

def prim(g, start):

    selected = [False] * g.n
    selected[start] = True

    total_weight = 0

    print("Prim MST 간선")

    for _ in range(g.n - 1):

        min_weight = INF
        u = -1
        v = -1

        for i in range(g.n):

            if selected[i]:

                for j in range(g.n):

                    if (not selected[j] and
                        g.adj_mat[i][j] != 0):

                        if g.adj_mat[i][j] < min_weight:

                            min_weight = g.adj_mat[i][j]
                            u = i
                            v = j

        selected[v] = True
        total_weight += min_weight

        print(f"{u} - {v} : {min_weight}")

    print("총 가중치 :", total_weight)

g = GraphType()

insert_edge(g, 0, 1, 10)
insert_edge(g, 0, 2, 6)
insert_edge(g, 0, 3, 5)
insert_edge(g, 1, 3, 15)
insert_edge(g, 2, 3, 4)

prim(g, 0)