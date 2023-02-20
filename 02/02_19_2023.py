# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    if not root.left and not root.right: return [[root.val]]

    answer = []
    direction = 1

    queue = deque([root])
    while queue:
      level = []
      for i in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
      answer.append(level[::direction])
      direction *= -1
      
    return answer
