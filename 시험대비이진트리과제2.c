#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

typedef struct TreeNode{
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
} TreeNode;

void preorder(TreeNode *root){
    if (root==NULL){
        return;
    }
    printf("%d",root->data);
    preorder(root->left);
    preorder(root->right);
}
void inorder(TreeNode *root){
    if (root==NULL){
        return ;
    }
    inorder(root->left);
    printf("%d",root->data);
    inorder(root->right);
}
void postorder(TreeNode *root){
    if (root==NULL){
        return ;
    }
    postorder(root->left);
    postorder(root->right);
    printf("%d",root->data);
}

int main(){
    TreeNode *A, *B, *C, *D, *E, *F;
    A=(TreeNode*)malloc(sizeof(TreeNode));
    B=(TreeNode*)malloc(sizeof(TreeNode));
    C=(TreeNode*)malloc(sizeof(TreeNode));
    D=(TreeNode*)malloc(sizeof(TreeNode));
    E=(TreeNode*)malloc(sizeof(TreeNode));
    F=(TreeNode*)malloc(sizeof(TreeNode));



    D->data=4;
    D->left=NULL;
    D->right=NULL;

    E->data=17;
    E->left=NULL;
    E->right=NULL;

    F->data=25;
    F->left=NULL;
    F->right=NULL;

    C->data=20;
    C->left=E;
    C->right=F;

    B->data=8;
    B->left=D;
    B->right=NULL;

    A->data=15;
    A->left=B;
    A->right=C;
}