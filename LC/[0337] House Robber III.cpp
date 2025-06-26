/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    unordered_map<TreeNode*, int> Flag1;
    unordered_map<TreeNode*, int> Flag0;

    int DFS(TreeNode * node, int flag){//flag=1: can choose, flag=0, cannot choose
        if(node == NULL) return 0;
        if(flag==1 && Flag1.find(node) != Flag1.end()) return Flag1[node];
        if(flag==0 && Flag0.find(node) != Flag0.end()) return Flag0[node];
        int ret;
        if(flag==0){
            ret = DFS(node->left, 1)+DFS(node->right, 1);
        }else{
            int option1 = node->val + DFS(node->left, 0) + DFS(node->right, 0);
            int option2 = DFS(node->left, 1)+DFS(node->right, 1);
            ret = max(option1, option2);

        }

        if(flag==1) Flag1[node] = ret;
        if(flag==0) Flag0[node] = ret;
        return ret;
    }
public:
    int rob(TreeNode* root) {
        return DFS(root, 1);        
    }
};