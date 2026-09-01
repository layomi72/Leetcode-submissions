# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []

        def dfs(root):
            stack = [root]
            visited = [False]

            if not root:
                return self.answer


            while stack:
                curr, seen = stack.pop(), visited.pop()
                if curr:
                    if seen:
                        self.answer.append(curr.val)

                    else:
                        stack.append(curr); visited.append(True)
                        stack.append(curr.right); visited.append(False)
                        stack.append(curr.left); visited.append(False)

        dfs(root)

        return self.answer