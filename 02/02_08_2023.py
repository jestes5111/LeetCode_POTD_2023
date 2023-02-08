class Solution:
  def jump(self, nums: List[int]) -> int:
    if len(nums) <= 1: return 0

    left, right = 0, nums[0]
    jumps = 1
    while right < len(nums) - 1:
      jumps += 1
      next = max(i + nums[i] for i in range(left, right + 1))
      left, right = right, next
    return jumps
