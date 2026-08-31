# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        
        def bfs(root):
            queue = deque([root])
            while len(queue) > 0:
                if not root:
                    return self.ans
                    
                n = len(queue)
                
                for i in range(n):
                    x = queue.popleft()

                    if i == n - 1:
                        self.ans.append(x.val)
                    
                    if x.left:
                        queue.append(x.left)

                    if x.right:
                        queue.append(x.right)
        bfs(root)

        return self.ans
