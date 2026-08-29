# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        def invert(root):
            if not root:
                return 

            invert(root.right)
            invert(root.left)
            
            right = root.right
            left = root.left

            root.right = left
            root.left = right

        invert(root)

        return head
