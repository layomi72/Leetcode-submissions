# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def travel(root):
            if not root:
                return
            
            travel(root.left)
            array.append(root.val)
            travel(root.right)

            return
        
        travel(root)

        return array[k-1]