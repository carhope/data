#include <stdio.h>
#include <stdlib.h>

#define MAX_VERTICES 6
#define MAX 6
#define TRUE 1
#define FALSE 0

int visited[MAX]; 
char* city_names[] = {"서울", "일본", "방콕", "파리", "런던", "뉴욕"}; // 도시 이름 매칭용

typedef struct GraphNode {
    int vertex;               
    struct GraphNode* link;   
} GraphNode;

typedef struct {
    int data[MAX_VERTICES];
    int front, rear;
} QueueType;

typedef struct GraphType {
    int n; 
    int adj_mat[MAX][MAX];           
    GraphNode* adj_list[MAX_VERTICES]; 
} GraphType;


void init(GraphType* g) {
    g->n = MAX;
    for (int i = 0; i < MAX; i++) {
        visited[i] = FALSE;
        g->adj_list[i] = NULL; 
        for (int j = 0; j < MAX; j++)
            g->adj_mat[i][j] = 0;
    }
}

void queue_init(QueueType* q) { q->front = q->rear = 0; }
int is_empty(QueueType* q) { return (q->front == q->rear); }
void enqueue(QueueType* q, int item) {
    q->rear = (q->rear + 1) % MAX_VERTICES;
    q->data[q->rear] = item;
}
int dequeue(QueueType* q) {
    q->front = (q->front + 1) % MAX_VERTICES;
    return q->data[q->front];
}

// --- 간선 삽입 (행렬 & 리스트 둘 다 수행) ---
void insert_edge(GraphType* g, int u, int v) {
    // 1. 행렬 삽입
    g->adj_mat[u][v] = 1;
    g->adj_mat[v][u] = 1;

    // 2. 리스트 삽입 
    GraphNode* node = (GraphNode*)malloc(sizeof(GraphNode));
    node->vertex = v;
    node->link = g->adj_list[u];
    g->adj_list[u] = node;

    node = (GraphNode*)malloc(sizeof(GraphNode));
    node->vertex = u;
    node->link = g->adj_list[v];
    g->adj_list[v] = node;
}

// --- 미션 구현 함수들 ---

void dfs_list(GraphType* g, int v) {
    visited[v] = TRUE;
    printf("%s -> ", city_names[v]);
    for (GraphNode* w = g->adj_list[v]; w != NULL; w = w->link) {
        if (!visited[w->vertex]) dfs_list(g, w->vertex);
    }
}

// [미션 3-2] BFS (인접 리스트 버전)
void bfs_list(GraphType* g, int v) {
    QueueType q;
    queue_init(&q);
    visited[v] = TRUE;
    enqueue(&q, v);
    while (!is_empty(&q)) {
        v = dequeue(&q);
        printf("%s -> ", city_names[v]);
        for (GraphNode* w = g->adj_list[v]; w != NULL; w = w->link) {
            if (!visited[w->vertex]) {
                visited[w->vertex] = TRUE;
                enqueue(&q, w->vertex);
            }
        }
    }
}


void dfs_mat(GraphType* g, int v) {
    visited[v] = TRUE;
    printf("정점 %d -> ", v);
    for (int w = 0; w < g->n; w++) {
        if (g->adj_mat[v][w] == 1 && !visited[w]) dfs_mat(g, w);
    }
}

int main() {
    GraphType g;
    init(&g);

    insert_edge(&g, 0, 1); insert_edge(&g, 0, 2);
    insert_edge(&g, 1, 3); insert_edge(&g, 2, 3);
    insert_edge(&g, 2, 4); insert_edge(&g, 3, 4);
    insert_edge(&g, 3, 5); insert_edge(&g, 4, 5);



    
    printf("--- [기존] DFS 행렬 탐색 시작 ---\n");
    for(int i=0; i<MAX; i++) visited[i] = FALSE;
    dfs_mat(&g, 0); printf("탐색 종료\n");

    printf("--- [기존] 직항 확인 (서울->런던) ---\n");
    if (g.adj_mat[1][4] == 1) printf("결과 : 직항 있음\n");
    else printf("결과 : 직항 없음\n");

    printf("--- [기존] 서울 연결 도시 검색 ---\n");
    int seoulcity = 0;
    for (int i = 0; i < MAX; i++) {
        if (g.adj_mat[0][i]) {
            seoulcity++;
            printf("%s ", city_names[i]);
        }
    }
    printf("\n서울과 총 %d개 연결\n", seoulcity);
    // --- 미션 3: 인접 리스트 기반 탐색 ---
    printf("### 미션 3-1: 인접 리스트 DFS (도시 이름) ###\n");
    for(int i=0; i<MAX; i++) visited[i] = FALSE;
    dfs_list(&g, 0); printf("종료\n\n");

    printf("### 미션 3-2: 인접 리스트 BFS (도시 이름) ###\n");
    for(int i=0; i<MAX; i++) visited[i] = FALSE;
    bfs_list(&g, 0); printf("종료\n\n");

    printf("### 미션 3-3: 데이터 매칭 (인덱스 3 연결) ###\n");
    printf("파리와 연결된 도시: ");
    for (GraphNode* w = g.adj_list[3]; w != NULL; w = w->link) {
        printf("%s ", city_names[w->vertex]);
    }
    printf("\n\n");
    return 0;
}