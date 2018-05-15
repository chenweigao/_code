#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    char val;
    int count=1;
    TreeNode *left;
    TreeNode *right;
    TreeNode(char val){
        this -> val = val;
    }
};
ostream& operator<<(ostream& st, TreeNode& node){
    st << node.val << ':' << node.count;
    return st;
}
class  Solution{
public:
    TreeNode *root;

    void insert(int val, TreeNode * & root){
//        TreeNode *node = new TreeNode(val);
        if(root == nullptr){
            root = new TreeNode(val);
        }

        else if(val == root->val){
            root -> count += 1;
        }

        else if(val < root->val){
            insert(val, root->left);
        }
        else
            insert(val, root->right);
    }

    void  create(vector<char> &a){
        for(int val : a)
        {
            insert(val, this->root);
        }
    }

    void traverse(vector<TreeNode> &res, TreeNode* root){
        if(root == nullptr){
            return;
        }
        traverse(res, root->left);
        res.push_back(*root);
        traverse(res, root->right);
    }

    vector<TreeNode> inorderTraverse(){
        vector<TreeNode> res;
        traverse(res, root);
        return  res;
    }

};
int main() {
    vector<char> a = {'a', 'b','a'};
    auto t = new Solution();
    t->create(a);
    auto answer = t->inorderTraverse();
    for(auto i: answer){
        cout << i <<endl;
    }

//    std::cout << "Hello, World!" << std::endl;
    return 0;
}