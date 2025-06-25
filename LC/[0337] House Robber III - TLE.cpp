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

    int DFS(TreeNode * node, int flag){//flag=1: can choose, flag=0, cannot choose
        if(node == NULL) return 0;
        if(flag==0){
            return DFS(node->left, 1)+DFS(node->right, 1);
        }else{
            int option1 = node->val + DFS(node->left, 0) + DFS(node->right, 0);
            int option2 = DFS(node->left, 1)+DFS(node->right, 1);
            return max(option1, option2);

        }
    }
public:
    int rob(TreeNode* root) {
        return DFS(root, 1);        
    }
};