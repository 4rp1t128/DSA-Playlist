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
void postOrder(Node *node)
{
    if (node == NULL)
    {
        return;
    }
    postOrder(node->left);
    postOrder(node->right);
    cout << " " << node->data << " ";
}

int main()
{
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->right = new Node(4);
    postOrder(root);
    return 0;
}
