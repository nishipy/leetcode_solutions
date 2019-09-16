# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution: 
    def sortedArrayToBST(self, x):
        if not x:
            return None
        
        mid_i = len(x) // 2
        tree = TreeNode(x[mid_i])
        tree.left = self.sortedArrayToBST(x[:mid_i])
        tree.right = self.sortedArrayToBST(x[mid_i+1:])

        return tree