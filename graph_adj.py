# 1. 정점 데이터와 빈 인접 리스트 생성
vertex = ['A', 'B', 'C', 'D']
adj_list = [[] for _ in range(4)]

# 2. 간선 삽입 (번호표 추가)
def insert_edge(lst, u, v):
    lst[u].append(v)
    lst[v].append(u)

# 3. 인접 리스트 출력 함수
def print_adj_list(v_names, a_list):
    print("--- 그래프 인접 리스트 출력 (Python) ---")
    for i in range(len(v_names)):
        # 인접한 정점 번호들을 이름으로 변환하여 보기 좋게 출력
        neighbors = [v_names[neighbor_idx] for neighbor_idx in a_list[i]]
        print(f"정점 {v_names[i]}: {' -> '.join(neighbors)}")

# 메인
if __name__ == "__main__":
    # 데이터 입력
    insert_edge(adj_list, 0, 1)  # A - B
    insert_edge(adj_list, 0, 2)  # A - C
    insert_edge(adj_list, 1, 3)  # B - D
    insert_edge(adj_list, 2, 3)  # C - D

    # 출력 호출
    print_adj_list(vertex, adj_list)