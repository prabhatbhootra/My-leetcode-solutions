# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left == None and root.right == None:
            return -1
        min1 = root.val
        self.min2 = float('inf')
        def dfs(node):
            if node.val > min1 and node.val < self.min2:
                self.min2 = node.val
            if node.left != None:
                dfs(node.left)
            if node.right != None:
                dfs(node.right)
        dfs(root)
        if self.min2 == float('inf'):
            return -1
        return self.min2
