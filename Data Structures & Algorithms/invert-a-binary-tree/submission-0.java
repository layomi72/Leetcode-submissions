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
    public TreeNode invertTree(TreeNode root) {
        TreeNode left1 = null;
        TreeNode right1 = null;
        if (root == null){
            return root;
        }
        else{
            left1 = root.left;
            right1 = root.right;
            root.right = left1;
            root.left = right1;
            invertTree(root.left);
            invertTree(root.right);
    }
    return root;
}
}