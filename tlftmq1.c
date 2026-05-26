#include <stdio.h>
#include <stdlib.h>

// 이진트리의 노드를 표현하는 구조체 정의
typedef struct TreeNode {
    int data;                // 노드에 저장될 데이터
    struct TreeNode *left;    // 왼쪽 자식 포인터
    struct TreeNode *right;   // 오른쪽 자식 포인터
} TreeNode;


/* ==========================
   노드 개수 계산
   ========================== */
int Total(TreeNode* root) {
    // 노드가 없으면 0개
    if (root == NULL)
        return 0;

    // 자기 자신(1) + 왼쪽 서브트리 + 오른쪽 서브트리
    return root->data + Total(root->left) + Total(root->right);
}

/* ==========================
   단말(leaf) 노드 개수 계산
   ========================== */
int count_leaf(TreeNode* root) {
    // 노드가 없으면 단말도 없음
    if (root == NULL)
        return 0;

    // 왼쪽, 오른쪽 자식이 모두 없으면 단말 노드
    if (root->left == NULL && root->right == NULL)
        return root->data;


    return count_leaf(root->left) + count_leaf(root->right);
}


int calc_height(TreeNode* root) {

    if (root == NULL)
        return 0;


    int left_h = calc_height(root->left);
    int right_h = calc_height(root->right);


    return (left_h > right_h ? left_h : right_h) + root->data;
}


int main() {

    TreeNode *A, *B, *C, *D, *E, *F, *G;


    A = (TreeNode*)malloc(sizeof(TreeNode));
    B = (TreeNode*)malloc(sizeof(TreeNode));
    C = (TreeNode*)malloc(sizeof(TreeNode));
    D = (TreeNode*)malloc(sizeof(TreeNode));
    E = (TreeNode*)malloc(sizeof(TreeNode));
    F = (TreeNode*)malloc(sizeof(TreeNode));
    G = (TreeNode*)malloc(sizeof(TreeNode));





    A->data = 10;
    B->data = 20;
    C->data = 30;
    D->data = 40;
    E->data = 50;
    F->data = 60;
    G->data = 70;
    
    A->left = B;
    A->right = C;

    B->left = D;
    B->right = E;

    C->left = F;
    C->right = NULL;

    D->left = NULL;
    D->right = NULL;

    E->left = NULL;
    E->right = NULL;

    F->left =NULL;
    F->right = G;

    G->left = NULL;
    G->right = NULL;

    // ===== 결과 출력 =====
    printf("전체 업무 비용 합계   : %d\n", Total(A));
    printf("최종 처리 업무 합   : %d\n", count_leaf(A));
    printf("최대 누적 처리 비용   : %d\n", calc_height(A));

    // 메모리 해제 (자식 → 부모 순서)
    free(D);
    free(E);
    free(B);
    free(C);
    free(A);

    return 0;
}
