import queue

# 0. 도시 이름 및 인덱스 정의
# 0:서울, 1:일본, 2:방콕, 3:파리, 4:런던, 5:뉴욕
vtx = ["서울", "일본", "방콕", "파리", "런던", "뉴욕"]
n = len(vtx)

# 1. 행렬 및 리스트 초기화
adj_mat = [[0] * n for _ in range(n)]
adj_list = [[] for _ in range(n)]

# 2. 간선 삽입 함수 (행렬과 리스트를 동시에 업데이트)
def insert_edge(u, v):
    # 행렬 업데이트
    adj_mat[u][v] = 1
    adj_mat[v][u] = 1
    # 리스트 업데이트 (요청된 순서를 위해 방콕부터 탐색되도록 순서 조절)
    adj_list[u].append(v)
    adj_list[v].append(u)

# 3. 데이터 입력 (출력 순서에 최적화된 삽입)
insert_edge(0, 2) # 서울-방콕
insert_edge(0, 1) # 서울-일본
insert_edge(2, 4) # 방콕-런던
insert_edge(2, 3) # 방콕-파리
insert_edge(4, 5) # 런던-뉴욕
insert_edge(4, 3) # 런던-파리
insert_edge(5, 3) # 뉴욕-파리
insert_edge(3, 1) # 파리-일본

# --- [기존] 로직 출력 ---
print("---  직항 확인 (서울->런던) ---")
# 서울(0), 런던(4)
if adj_mat[0][4] == 1:
    print("결과 : 직항 있음")
else:
    print("결과 : 직항 없음")

print("---  서울 연결 도시 검색 ---")
seoul_connected = []
for i in range(n):
    if adj_mat[0][i] == 1:
        seoul_connected.append(vtx[i])
print(f"{' '.join(seoul_connected)}")
print(f"서울과 총 {len(seoul_connected)}개 연결")

# --- [미션 3-1] DFS 구현 (재귀 방식) ---
def DFS_AL(v, visited):
    visited[v] = True
    print(vtx[v], end=' -> ')
    for neighbor in adj_list[v]:
        if not visited[neighbor]:
            DFS_AL(neighbor, visited)

print("\n### 미션 3-1: 인접 리스트 DFS (도시 이름) ###")
visited_dfs = [False] * n
DFS_AL(0, visited_dfs)
print("종료")

# --- [미션 3-2] BFS 구현 (표준 큐 방식) ---
def BFS_AL(s):
    visited = [False] * n
    Q = queue.Queue()
    visited[s] = True
    Q.put(s)
    
    while not Q.empty():
        curr = Q.get()
        print(vtx[curr], end=' -> ')
        for neighbor in adj_list[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                Q.put(neighbor)

print("\n### 미션 3-2: 인접 리스트 BFS (도시 이름) ###")
BFS_AL(0)
print("종료")

# --- [미션 3-3] 데이터 매칭 ---
print("\n### 미션 3-3: 데이터 매칭 (인덱스 3 연결) ###")
# 인덱스 3은 '파리'
paris_neighbors = [vtx[i] for i in adj_list[3]]
print(f"파리와 연결된 도시: {' '.join(paris_neighbors)}")