class Solution:
  def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
      middle = left + (right - left) // 2
      if nums[middle] == target: 
        return middle
      elif nums[middle] > target:
        right = middle
      else:
        left = middle + 1
    return left + 1 if nums[left] < target else left
