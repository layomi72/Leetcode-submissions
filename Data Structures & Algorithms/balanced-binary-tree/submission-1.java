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
    public boolean isBalanced(TreeNode root) {
       if (root == null){
        return true;
       }
       else{
        int ls = no(root.left);
        int rs = no(root.right);

        int diff = ls - rs;

        if(Math.abs(diff) >1){
            return false;
        }
        boolean lft = isBalanced(root.left);
        boolean rft = isBalanced(root.right);
        return lft && rft;
       }
       
        }
    private int no (TreeNode root){
            if (root == null){
                return 0;
            }
            else{
                int ls = no(root.left);
                int rs = no(root.right);
                return 1 + Math.max(ls,rs);
            }
        }
    }

