MAX = 5
INF = 10**9


class GraphType:
    def __init__(self):
        self.n = MAX
        self.adj_mat = [[0 for _ in range(MAX)] for _ in range(MAX)]


def insert_edge(g, u, v, weight):
    g.adj_mat[u][v] = weight
    g.adj_mat[v][u] = weight


def print_distance(dist):
    print("정점\t거리")

    for i in range(MAX):
        if dist[i] == INF:
            print(f"{i}\tINF")
        else:
            print(f"{i}\t{dist[i]}")


def dijkstra(g, start):
    # 1-2. 주어진 코드 속 dist = [INF] * g.n 에서 dist 배열은 어떤 역할을 하는가?
    dist = [INF] * g.n

    # 1-3. 주어진 코드 속 visited = [False] * g.n 에서 visited 배열은 어떤 역할을 하는가?
    visited = [False] * g.n

    # 1-4. 주어진 코드 속 dist[start] = 0은 어떤 의미를 나타내는가?
    dist[start] = 0

    for _ in range(g.n):
        min_dist = INF
        u = -1

        for i in range(g.n):
            # 1-5. 주어진 코드 속 if not visited[i] and dist[i] < min_dist: 조건문의 의미를 설명해보자.
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        # 1-6. 주어진 코드 속 visited[u] = True는 어떤 의미를 나타내는가?
        visited[u] = True

        for v in range(g.n):
            # 1-7. 주어진 코드 속 weight = g.adj_mat[u][v]는 무엇을 확인하기 위한 코드인가?
            weight = g.adj_mat[u][v]

            # 1-8. 주어진 코드 속 if weight != 0 and not visited[v]: 조건문의 의미를 설명해보자.
            if weight != 0 and not visited[v]:

                # 1-9. 주어진 코드 속 if dist[u] + weight < dist[v]: 조건문은 어떤 상황을 의미하는가?
                if dist[u] + weight < dist[v]:

                    # 1-10. 주어진 코드 속 dist[v] = dist[u] + weight는 왜 실행되는가?
                    dist[v] = dist[u] + weight

    print_distance(dist)


g = GraphType()

insert_edge(g, 0, 1, 4)
insert_edge(g, 0, 2, 2)
insert_edge(g, 1, 2, 1)
insert_edge(g, 1, 3, 5)
insert_edge(g, 2, 3, 8)
insert_edge(g, 2, 4, 10)
insert_edge(g, 3, 4, 2)

dijkstra(g, 0)