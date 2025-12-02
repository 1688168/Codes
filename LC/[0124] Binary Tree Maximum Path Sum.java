import java.lang.Math;

/**
 * Definition for a binary tree node.
 * This class structure is required for Java solutions.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    // 1. Global variable to store the final maximum path sum found across the entire tree.
    // Must be initialized to a very small number (Integer.MIN_VALUE) since nodes can have negative values.
    private int maxPathSumGlobal = Integer.MIN_VALUE; //java min integer value

    /**
     * @brief Calculates the maximum path sum that STARTS at 'node' and goes DOWNWARD.
     * It also updates the global maximum path sum (including "V" paths) found so far.
     * @param node The current TreeNode.
     * @return The maximum path sum that continues up to the parent.
     */
    private int maxDownPath(TreeNode node) {
        // Base case: null node contributes a sum of 0 to the path.
        if (node == null) {
            return 0;
        }

        // Recursively find the max path sum that starts from the left/right child and goes downward.
        // We only consider positive contributions from children. If left/right sum is negative, we take 0.
        int leftSum = Math.max(0, maxDownPath(node.left));
        int rightSum = Math.max(0, maxDownPath(node.right));
        
        // --- 1. Calculate the MAX-TURN Path (Path that starts and ends within the subtree rooted at 'node') ---
        // The max path sum that uses this node as the peak (the 'V' shape).
        // This path is node.val + leftSum + rightSum.
        int maxTurnSum = node.val + leftSum + rightSum;
        
        // Update the global maximum path sum found so far.
        this.maxPathSumGlobal = Math.max(this.maxPathSumGlobal, maxTurnSum);
        
        // --- 2. Calculate the MAX-DOWN Path (Path that continues UPWARD from 'node') ---
        // The path sum that we return to the parent must be a straight line (node + max of one child).
        // This calculation is simpler than your C++ logic due to the Math.max(0, ...) above.
        return node.val + Math.max(leftSum, rightSum);
    }


    public int maxPathSum(TreeNode root) {
        // Initialize the global result to the minimum possible integer value
        this.maxPathSumGlobal = Integer.MIN_VALUE; 
        
        // Start the recursive traversal
        maxDownPath(root);
         
        return this.maxPathSumGlobal;
    }
}