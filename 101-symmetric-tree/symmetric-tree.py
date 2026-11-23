class Solution:
    def isSymmetric(self, root):
        def dfs(a, b):
            if not a or not b:
                return a == b

            if a.val != b.val:
                return False

            return dfs(a.left, b.right) and dfs(a.right, b.left)

        return dfs(root.left, root.right) if root else True