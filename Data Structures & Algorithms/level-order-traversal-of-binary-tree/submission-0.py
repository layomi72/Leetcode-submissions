# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.order = []

        def bfs(root):
            if not root:
                return self.order
            queue = deque([root])
            while len(queue) > 0:
                n = len(queue)
                ans = []
                for i in range(n):
                    x = queue.popleft()
                    ans.append(x.val)
                    if x.left:
                        queue.append(x.left)

                    if x.right:
                        queue.append(x.right)
                
                self.order.append(ans)

        bfs(root)

        return self.order