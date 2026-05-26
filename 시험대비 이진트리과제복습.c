#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
typedef struct TreeNode{
    int data;
    struct TreeNode * left;
    struct TreeNode * right;

} TreeNode;
int main(){
    int user;
    scanf("%d",&user);
    TreeNode * A, *B, *C, *D, *E;

    A= (TreeNode*)malloc(sizeof(TreeNode));
    B= (TreeNode*)malloc(sizeof(TreeNode));
    C= (TreeNode*)malloc(sizeof(TreeNode));
    D= (TreeNode*)malloc(sizeof(TreeNode));
    E= (TreeNode*)malloc(sizeof(TreeNode));

    A ->data=10;
    A->left=B;
    A->right=C;

    B->data=20;
    B->left=D;
    B->right=NULL;
    
    C->data=15;
    C->left=E;
    C->right=NULL;

    D->data=40+user;
    D->left=NULL;
    D->right=NULL;

    E->data=35;
    E->left=NULL;
    E->right=NULL;


    printf("%d\n",A->data+A->left->data+A->left->left->data);
    printf("%d\n",A->data);

    free(A);
    free(B);
    free(C);
    free(D);
    free(E);
}

