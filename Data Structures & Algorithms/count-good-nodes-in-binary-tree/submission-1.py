# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodnodes = 0

        def good(root, maxval):
            if not root:
                return None

            if root.val >= maxval:
                self.goodnodes += 1
                
            maxval = max(maxval,root.val)

            if root.left:
                good(root.left,maxval)

            if root.right:
                good(root.right,maxval)
           
           

        good(root, -float("inf"))

        return self.goodnodes
