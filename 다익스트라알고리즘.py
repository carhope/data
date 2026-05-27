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
'''[STEP 0 ] 인접 행렬 이해하기
이번 수업에서는 그래프를 인접 행렬 방식으로 표현한다. adj_mat[u][v]는 정점 u에서 정점 v로 가는 간선의 가중치를 의미한다.
typedef struct GraphType {
 	int n;
 	int adj_mat[MAX][MAX];
 } GraphType;

 void insert_edge(GraphType* g, int u, int v, int weight) {
 	g->adj_mat[u][v] = weight;
 	g->adj_mat[v][u] = weight;
 }

0-1. 주어진 코드 속 adj_mat[u][v] = weight는 어떤 의미를 나타내는가?
정점 u에서 정점 v로 가는 가중치를 weight로 저장한다


0-2. 주어진 코드 속 adj_mat[u][v] = 0을 간선 없음으로 사용하면 어떤 장점과 한계가 있는가?
간선이 없는 상태를 쉽게 표현할수 있음
But. 가중치가 실제로 0인 간선과 구별할 수 없음


0-3. insert_edge 함수에서 g->adj_mat[v][u] = weight를 함께 실행하는 이유는 무엇인가?
u→v 로 갈 수 있으면 v→u 로도 같은 가중치로 이동할 수 있도록 양쪽 값을 모두 저장



1. 다(many)익스트라(이커) 알고리즘
1-1. 사용할 그래프
다익스트라 알고리즘은 음수 가중치가 없는 그래프에서 사용한다. 아래 그래프에서 시작 정점은 0이다.

1-2. 인접 행렬 완성하기
위 그래프를 보고 인접 행렬을 완성하시오. 간선이 없으면 0을 적는다.


1-3. 주요 변수 정리하기
변수
내가 이해한 역할
dist[i]
시작정점에서 i까지 알려진 최단 거리 
visited[i]
시작정점부터 정점i까지 확정되어있는지 여부 
u
현재단계에서 선택된 정점 
v
u와 연결되어있는지 확인하는 정점 
weight
u와v의 간선의 가중치 
INF
큰 값 


1-4. 코드 의미 분석
dist = [INF] * g.n
 visited = [False] * g.n
 dist[start] = 0

 for _ in range(g.n):
 	min_dist = INF
 	u = -1

 	for i in range(g.n):
     	if not visited[i] and dist[i] < min_dist:
         	min_dist = dist[i]
         	u = i

 	if u == -1:
     	break

 	visited[u] = True

 	for v in range(g.n):
     	weight = g.adj_mat[u][v]

     	if weight != 0 and not visited[v]:
         	if dist[u] + weight < dist[v]:
             	dist[v] = dist[u] + weight

1-1. 다익스트라 알고리즘은 어떤 방식으로 시작 정점에서 다른 정점까지의 최단거리를 찾아가는가?
인접행렬리스트


1-2. 주어진 코드 속 dist = [INF] * g.n에서 dist 배열은 어떤 역할을 하는가?
정해진 정점에서의 최단거리 (range)


1-3. 주어진 코드 속 visited = [False] * g.n에서 visited 배열은 어떤 역할을 하는가?
최단거리가 정해진(방문한) 정점(wjdwja)을 저장



1-4. 주어진 코드 속 if not visited[i] and dist[i] < min_dist: 조건문의 의미를 설명해보자.
정점 i 가 정점을 저장하는 리스트에 저장이 안되어 있으면서 min_dist(현재 연결되어있는 그 정점의 최솟값)의 값보다 작으면이라는 조건


1-5. 주어진 코드 속 if weight != 0 and not visited[v]: 조건문의 의미를 설명해보자.
가중치가 0이 아니고 정점v 가 방문이 안되어있다면


1-6. 주어진 코드 속 if dist[u] + weight < dist[v]: 조건문은 어떤 상황을 의미하는가?
정점 v로 가는 기존경로보다 정점 u를 거쳐서가는 경로가 더 짧은 상황



1-5. 단계별 변수 변화 기록하기
시작 정점 0에서 출발할 때 dist와 visited가 어떻게 변하는지 기록하시오.
단계
선택 정점 u
dist 배열
visited 배열
값이 바뀐 이유
초기
-
[0, INF, INF, INF, INF]
[F, F, F, F, F]
시작 정점 0의 거리를 0으로 설정
1
 0
 [0,4,2,INF,INF]
[T,F,F,F,F] 
 0에서 갈수 있는 경로중 최단거리 갱신
2
2 
 [0,3,2,10,12]
 [T,F,T,F,F]
 2에서 갈수 있는 경로중 최단거리 갱신
3
1 
 [0,3,2,8,10]
 [T,T,T,F,F]
 1에서 갈수 있는 경로중 최단거리 갱신
4
3 
 [0,3,2,8,10]
 [T,T,T,T,F]
 값이 안바뀜
5
4 
 [0,3,2,8,10]
 [T,T,T,T,T]
값이 안바뀜'''

