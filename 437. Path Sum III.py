# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0
        self.dfs(root, sum)
        return self.ans

    def dfs(self, node, sum):
        if node is None:
            return
        self.helper(node, sum)
        self.dfs(node.left, sum)
        self.dfs(node.right, sum)
    
    def helper(self, node, sum):
        if node is None:
            return
        if node.val == sum:
            self.ans += 1
        self.helper(node.left, sum-node.val)
        self.helper(node.right, sum-node.val)

