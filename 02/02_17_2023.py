# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  previous = -float('inf')
  answer = float(inf)

  def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    if root.left: self.minDiffInBST(root.left)
    self.answer = min(self.answer, root.val - self.previous)
    self.previous = root.val
    if root.right: self.minDiffInBST(root.right)
    return self.answer
