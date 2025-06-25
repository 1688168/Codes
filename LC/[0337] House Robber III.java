/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private Map<TreeNode, Integer> cache1 = new HashMap<>();
    private Map<TreeNode, Integer> cache2 = new HashMap<>();
    private int rob(TreeNode root, boolean canRob){
        if(root==null) return 0;
        if(canRob && this.cache1.containsKey(root)) return this.cache1.get(root);
        if(!canRob && this.cache2.containsKey(root)) return this.cache2.get(root);
        int ret = 0;
        if(canRob){
            ret= Math.max(root.val+this.rob(root.left, false)+this.rob(root.right, false), this.rob(root.left, true)+this.rob(root.right, true));
        }else{
            ret = this.rob(root.left, true) + this.rob(root.right, true);
        }
        if(canRob) this.cache1.put(root, ret);
        if(!canRob) this.cache2.put(root, ret);
        return ret;
    }

    public int rob(TreeNode root) {
        return Math.max(root.val+this.rob(root.left, false)+this.rob(root.right, false), this.rob(root.left, true)+this.rob(root.right, true));
    }
}