#include <stdio.h>

#define MAX 4
#define INF 9999

typedef struct GraphType {
    int n;
    int adj_mat[MAX][MAX];
} GraphType;

void init(GraphType* g) {
    g->n = MAX;

    for (int i = 0; i < MAX; i++) {
        for (int j = 0; j < MAX; j++) {
            g->adj_mat[i][j] = 0;
        }
    }
}

void insert_edge(GraphType* g, int u, int v, int weight) {
    g->adj_mat[u][v] = weight;
    g->adj_mat[v][u] = weight;
}

void prim(GraphType* g, int start) {
    int selected[MAX] = {0};
    int total_weight = 0;

    selected[start] = 1;

    printf("Prim MST 간선\n");

    for (int count = 0; count < g->n - 1; count++) {
        int min = INF;
        int u = -1;
        int v = -1;

        for (int i = 0; i < g->n; i++) {
            if (selected[i]) {
                for (int j = 0; j < g->n; j++) {
                    if (!selected[j] && g->adj_mat[i][j] != 0) {
                        if (g->adj_mat[i][j] < min) {
                            min = g->adj_mat[i][j];
                            u = i;
                            v = j;
                        }
                    }
                }
            }
        }

        selected[v] = 1;
        total_weight += min;

        printf("%d - %d : %d\n", u, v, min);
    }

    printf("총 가중치 : %d\n", total_weight);
}

int main() {
    GraphType g;

    init(&g);

    insert_edge(&g, 0, 1, 10);
    insert_edge(&g, 0, 2, 6);
    insert_edge(&g, 0, 3, 5);
    insert_edge(&g, 1, 3, 15);
    insert_edge(&g, 2, 3, 4);

    prim(&g, 0);

    return 0;
}