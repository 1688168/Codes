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
    int ret = INT_MIN;
public:
     int MaxDownPath(TreeNode * node){//starting from node downward only, the max-sum path
            if(node==NULL) return 0;
            int leftSum = MaxDownPath(node->left);
            int rightSum = MaxDownPath(node->right);
            //for each node we evaluate a path with respect to current node
            int maxTurnSum = node->val;
            if(leftSum > 0) maxTurnSum += leftSum;
            if(rightSum > 0) maxTurnSum += rightSum;

            ret = max(ret, maxTurnSum);//global max path sum
            
            //considering current node as the starting node of a path
            if(leftSum<0 && rightSum < 0)//is there child branch > 0?
                return node->val;//no child branch can add value, return self
            else
                return max(leftSum, rightSum) + node->val;
        }


    int maxPathSum(TreeNode* root) {
        MaxDownPath(root);
         
        return ret;
    }
};