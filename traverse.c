#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct tree_node {
    int data;

    struct tree_node *left;
    struct tree_node *right;
}treenode;
int sum = 0;
int count = 0;

void preorder(treenode *root){
    if (root==NULL){
        return ;
    }
    printf("%d ",root->data);
    preorder(root->left);
    preorder(root->right);
}
void in(treenode *root){
    if (root==NULL){
        return;
    }
    in(root->left);
    if (root->left == NULL && root->right == NULL){
        sum += root -> data;
    }
    in(root->right);
}

void postorder(treenode *root){
    if (root ==NULL){
        return;
    }
    postorder(root->left);
    postorder(root->right);
    count++;


}
void pre(treenode *root){
    if (root==NULL){
        return ;
    }
    if (root->data > 16) {
        printf("%d ", root->data);
    }
    pre(root->left);
    pre(root->right);
}
int main(){
    treenode *A,*B,*C,*D,*E,*F;
    A = (treenode*)malloc(sizeof(treenode));
    B = (treenode*)malloc(sizeof(treenode));
    C = (treenode*)malloc(sizeof(treenode));
    D = (treenode*)malloc(sizeof(treenode));
    E = (treenode*)malloc(sizeof(treenode));
    F = (treenode*)malloc(sizeof(treenode));

    A->data =15;
    A->left =B;
    A->right =C;

    B->data =8;
    B->left =D;
    B->right=NULL;

    C->data =20;
    C->left =E;
    C->right=F;

    D->data =4;
    D->left =NULL;
    D->right =NULL;

    E->data = 17;
    E->left = NULL;
    E->right = NULL;

    F->data=25;
    F->left = NULL;
    F->right = NULL;

printf("%d %d %d\n",A->data,A->left->data,A->right->data);
printf("전위 순회 : ");
pre(A);
printf("\n");
printf("중위 순회 : ");
in(A);
printf("%d ", sum);
printf("\n");
printf("후위 순회 : ");
postorder(A);
printf("%d ", count);
free(A);
free(B);
free(C);
free(D);
free(E);
free(F);
}