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
public:
    int countNodes(TreeNode* root) {
        int h=0;
        TreeNode * node = root;
        while(node!=NULL){
            ++h;
            node = node->left;
        }

        int low = pow(2, h-1);
        int hi = pow(2, h)-1;

        while(low < hi){
            int mid = low+(hi-low+1)/2;
            if(hasK(root, mid)){
                low = mid;
            }else{
                hi = mid-1;
            }
        }

        return low;
        
    }

    bool hasK(TreeNode * root, int k){
        vector<int> path;
        while (k > 0){
            path.push_back(k);
            k = k/2;
        }
        for(int ii=path.size()-1; ii>=0; --ii){
            if(root==NULL) return false;
            if(ii==0) return true;
            if(path[ii-1] == path[ii]*2)
                root = root->left;
            else
                root = root->right;
        }

        return false;
    }
};