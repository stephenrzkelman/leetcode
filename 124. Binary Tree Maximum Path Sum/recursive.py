# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSumConnectedToRoot(self, root: Optional[TreeNode]) -> int:
        leftPath = self.maxPathSumConnectedToRoot(root.left) if root.left is not None else 0
        rightPath = self.maxPathSumConnectedToRoot(root.right) if root.right is not None else 0
        return max(
            root.val,
            root.val + leftPath,
            root.val + rightPath
        )

    def maxPathThroughRoot(self, root: Optional[TreeNode]) -> int:
        leftMaxPath = max(0, self.maxPathSumConnectedToRoot(root.left)) if root.left is not None else 0
        rightMaxPath = max(0, self.maxPathSumConnectedToRoot(root.right)) if root.right is not None else 0
        return root.val + leftMaxPath + rightMaxPath

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        paths_to_compare = [self.maxPathThroughRoot(root)]
        if root.left is not None:
            paths_to_compare.append(self.maxPathSum(root.left))
        if root.right is not None:
            paths_to_compare.append(self.maxPathSum(root.right))
        return max(paths_to_compare)
