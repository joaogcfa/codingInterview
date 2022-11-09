# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.pathSumFrom(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def pathSumFrom(self, root, targetSum):
        if not root:
            return 0
        return (root.val == targetSum) + self.pathSumFrom(root.left, targetSum - root.val) + self.pathSumFrom(root.right, targetSum - root.val)
