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
    private boolean hasK(TreeNode node, int k){
        if(node == null) return false;
        //build the path
        ArrayList<Integer> path = new ArrayList<>();
        while(k>0){
            path.add(k);
            k /= 2;
        }

        //reverse the arrayList
        Collections.reverse(path);

        for(int ii=1; ii<path.size(); ++ii){
            int val = path.get(ii);
            if(val%2 != 0){
                node=node.right;
            }else{
                node=node.left;
            }
            if(node==null) return false;
        }

        //walk the path
        return true;
    }
    private int getHeight(TreeNode node){
        if(node == null) return 0;//no node -> height 0
        int hh=0;
        while(node != null){
            ++hh; //height starts from 1
            node=node.left;//next level -> keep moving left child
        }
        return hh;
    }
    public int countNodes(TreeNode root) {
        if(root == null) return 0; //no node at all

        //binary search
        int hh = getHeight(root);
        
        // -- define the range
        int ll = 1<<(hh-1);
        int rr = (1<<hh)-1;
        int ans=ll;
        while(ll<=rr){//binary search template
            int mm = ll+(rr-ll)/2;
            if(hasK(root, mm)){
                ans=mm;
                ll=mm+1;
            }else{
                rr=mm-1;
            }
        }

        return ans;
    }
    
}