#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int data;
    Node *left;
    Node *right;
    Node(int data)
    {
        this->data = data;
        left = NULL;
        right = NULL;
    }
};

void inOrder(Node* node){
    if(node == NULL){
        return;
    }
    inOrder(node->left);
    cout<<" "<<node->data<<" ";
    inOrder(node->right);
}

int main()
{
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->right = new Node(4);
    inOrder(root);
    return 0;
}
