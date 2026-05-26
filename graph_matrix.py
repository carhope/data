# 1. 4x4 행렬 생성 및 0으로 초기화
adj_mat = [[0] * 6 for _ in range(6)]

# 2. 간선 삽입 함수 정의
def insert_edge(mat, u, v):
    mat[u][v] = 1
    mat[v][u] = 1

# 3. 그래프 출력 함수 정의
def print_graph(mat):
    print("   A B C D E F")  # 상단 열 레이블
    vertices = ['A', 'B', 'C', 'D','E','F']
    
    for i in range(len(mat)):
        print(f"{vertices[i]} ", end="") # 좌측 행 레이블
        for j in range(len(mat[i])):
            print(f"{mat[i][j]} ", end="")
        print() # 줄바꿈

# 4. 데이터 입력
insert_edge(adj_mat, 0, 1) # 
insert_edge(adj_mat, 0, 2) #
insert_edge(adj_mat, 1, 4)
insert_edge(adj_mat, 1, 5) # 
insert_edge(adj_mat, 2, 3) # C-D
insert_edge(adj_mat,3,4)
insert_edge(adj_mat, 4, 5)

# 5. 결과 출력
print_graph(adj_mat)
if adj_mat[1][4]==1:
    print("연결되어 있다")
else:
    print("연결 안됌")
for k in range(len(adj_mat)):
    if adj_mat[0][k]==1:
        print(k)
r = 0
print("급식실과 연결된 곳 :",end='')
for p in range(len(adj_mat)):
    if adj_mat[p][4]==1 or adj_mat[4][p]==1 :
        r +=1
        if p==0:
            print("정문",end=',')
        if p==1:
            print("본관",end=',')
        if p==2:
            print("운동장",end=',')
        if p==3:
            print("체육괸",end=',')
        if p==5:
            print("도서관")
print(f'급식실에 연결된 인접 정점의 개수 :{r}')
