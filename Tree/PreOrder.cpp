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

void preOrder(Node *node)
{
    if (node == NULL)
    {
        return;
    }
    cout << " " << node->data << " ";
    preOrder(node->left);
    preOrder(node->right);
}

int main()
{
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->right = new Node(4);

    preOrder(root);
    return 0;
}
