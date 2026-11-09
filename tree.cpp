#include <queue>

const int MAX=1000;
struct BNode {
    char data;
    BNode* left;
    BNode* right;
};

BNode* root=nullptr;

void BFS(BNode *root){
    if (root==nullptr) return;
    queue<BNode*> q;
    q.push(root);
    while (!q.empty()){
        BNode* p=q.front();
        q.pop();
        if(p->left!=nullptr) q.push(p->left);
        if(p->right!=nullptr) q.push(p->right);
    }
}