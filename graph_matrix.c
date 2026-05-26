#include <stdio.h>

#define MAX 6

typedef struct GraphType {
    int n; // 정점의 개수
    int adj_mat[MAX][MAX]; // 연결 관계를 저장할 2차원 배열
     //4개수
} GraphType;

// 그래프 초기화: 배열의 모든 값을 0으로 설정
void init(GraphType* g) {
    g->n = MAX;
    for (int i = 0; i < MAX; i++)
        for (int j = 0; j < MAX; j++)
            g->adj_mat[i][j] = 0;
}

// 간선 삽입: 행렬의 대칭되는 위치에 1을 기록
void insert_edge(GraphType* g, int u, int v) {
    if (u >= g->n || v >= g->n) {
        printf("정점 번호 오류입니다.\n");
        return;
    }
    g->adj_mat[u][v] = 1;
    g->adj_mat[v][u] = 1;
}

// 인접 행렬 출력 함수
void print_adj_mat(GraphType* g) {
    printf("현재 그래프의 인접 행렬 상태:\n");
    for (int i = 0; i < g->n; i++) {
        for (int j = 0; j < g->n; j++) {
            printf("%d ", g->adj_mat[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int r;
    r =0;
    GraphType g;
    init(&g);
//0:정문, 1:본관, 2:운동장, 3:체육관, 4:급식실, 5:도서관
    insert_edge(&g, 0, 1);
    insert_edge(&g, 0, 2);
    insert_edge(&g, 1, 4);
    insert_edge(&g, 1, 5);
    insert_edge(&g, 2, 3);
    insert_edge(&g, 3, 4);
    insert_edge(&g, 4, 5);

    //1,4에 들어갔는지 확인해야함
    
    print_adj_mat(&g);
    if (g.adj_mat[1][4]==1){
        printf("연결 되어 있다.\n");
    }
    else{
        printf("나가");
    }
    for (int i=0;i!=MAX;i++){
        if (g.adj_mat[0][i]==1 || g.adj_mat[i][0]==1){
            printf("%d ",i);

        }
    }
    for (int j=0;j!=MAX;j++){
        if (g.adj_mat[j][4]==1 || g.adj_mat[4][j]==1){
            r += 1;
        }
    }
    printf("\n급식실 연결 인접 정점 개수 : %d\n",r);
    for (int k=0;k!=MAX;k++){
        if (g.adj_mat[k][4]==1 || g.adj_mat[4][k]==1){
            if (k == 0){
                printf("정문\n");
            }
            if (k ==1){
                printf("본관\n");
            }
            if (k==2){
                printf("운동장\n");
            }
            if (k==3){
                printf("체육관\n");
            }
            if (k==5){
                printf("도서관\n");
            }
        }
    }

    return 0;
}