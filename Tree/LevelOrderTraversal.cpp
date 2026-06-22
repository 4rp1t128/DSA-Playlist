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
void levelOrder(Node* root, vector<int>& ans){
    queue<Node*>q;
    if(root == nullptr) return;
    q.push(root);
    while(!q.empty()){
        Node* curr = q.front();
        q.pop();
        ans.push_back(curr->data);
        if(curr->left != NULL){
            q.push(curr->left);
        }
        if(curr->right != nullptr){
            q.push(curr->right);
        }
    }
}    
int main()
{
    vector<int>ans;
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    levelOrder(root,ans);
    for(int itr : ans){
        cout<<" "<<itr<<" ";
    }
    return 0;
}

