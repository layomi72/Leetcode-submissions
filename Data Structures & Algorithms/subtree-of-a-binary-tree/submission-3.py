# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # create a function to even find if the subRoot is present in the root 
        def present(root, subroot):
            if not root:
                return False

            if root.val == subRoot.val:
                if sameRoot(root,subRoot):
                    return True


                

            return present(root.right, subRoot) or present(root.left, subRoot)


        def sameRoot(p, q):
            if not p and not q:
                return True

            if p and not q:
                return False
            
            if q and not p:
                return False

            if p.val != q.val:
                return False

            return sameRoot(p.left,q.left) and sameRoot(p.right,q.right)

        if present(root,subRoot) == None:
            return False

        else:
            return present(root,subRoot)
        
