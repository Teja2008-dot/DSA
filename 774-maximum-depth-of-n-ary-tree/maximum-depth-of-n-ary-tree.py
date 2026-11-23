"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        def dfs(cur: 'Node' | None):
            if not cur:
                return 0
            
            best = 0
            for child in cur.children or []:
                best = max(best, dfs(child))
            return best + 1

        return dfs(root)
        