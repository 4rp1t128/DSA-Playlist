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

void preOderIterative(Node* root, vector<int>& ans){
    stack<Node*>st;
    if(root == nullptr) return;
    st.push(root);
    while(!st.empty()){
        Node* curr = st.top();
        st.pop();
        ans.push_back(curr->data);
        if(curr->right != NULL){
            st.push(curr->right);
        }
        if(curr->left != NULL){
            st.push(curr->left);
        }
    }

}

int main()
{
    Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);
    root->right->left = new Node(6);
    root->right->right = new Node(7);
    vector<int>ans;
    preOderIterative(root,ans);
    for(int itr : ans ){
        cout<<" "<<itr<<" ";
    }
    return 0;
}
