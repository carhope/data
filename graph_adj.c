#include <stdio.h>
#include <stdlib.h>

typedef struct GraphNode {
    int vertex;               // 인접 정점의 번호
    struct GraphNode* link;   // 다음 노드를 가리키는 포인터
} GraphNode;

typedef struct GraphType{
    GraphNode* adj_list[4];   // 헤드 포인터 배열
} GraphType;

// 그래프 초기화 함수: 모든 헤드 포인터를 NULL로 설정
void init_graph(GraphType* g) {
    for (int i = 0; i < 4; i++) {
        g->adj_list[i] = NULL; // 0번부터 3번까지 보관함을 모두 깨끗이 비웁니다.
    }
}

// 간선 삽입: 새로운 노드를 동적 할당하여 리스트 맨 앞에 추가
void insert_edge(GraphType* g, int u, int v) {
    GraphNode* node = (GraphNode*)malloc(sizeof(GraphNode));
    node->vertex = v;
    node->link = g->adj_list[u]; // 현재 헤드를 새 노드의 다음으로 연결
    g->adj_list[u] = node;       // 새 노드를 새로운 헤드로 지정
}

// 인접 리스트 출력 함수
void print_adj_list(GraphType* g) {
    char vertex_name[] = {'A', 'B', 'C', 'D'};
    for (int i = 0; i < 4; i++) {
        GraphNode* p = g->adj_list[i];
        printf("정점 %c의 인접 리스트: ", vertex_name[i]);
        while (p != NULL) {
            printf("-> %c ", vertex_name[p->vertex]);
            p = p->link;
        }
        printf("\n");
    }
}

int main() {
    GraphType g;
    init_graph(&g);

    // 0:A, 1:B, 2:C, 3:D
    
    // A - B 연결
    insert_edge(&g, 0, 1);
    insert_edge(&g, 1, 0);

    // A - C 연결
    insert_edge(&g, 0, 2);
    insert_edge(&g, 2, 0);

    // B - D 연결
    insert_edge(&g, 1, 3);
    insert_edge(&g, 3, 1);

    // C - D 연결
    insert_edge(&g, 2, 3);
    insert_edge(&g, 3, 2);

    printf("--- 그래프 인접 리스트 출력 ---\n");
    print_adj_list(&g);

    return 0;
}