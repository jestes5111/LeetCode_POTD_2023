class Solution:
  def singleNonDuplicate(self, nums: List[int]) -> int:
    if len(nums) == 1: return nums[0]

    low, high = 0, len(nums) - 1
    while low < high:
      mid = low + (high - low) // 2
      if ((mid % 2 == 1 and nums[mid - 1] == nums[mid]) or 
          (mid % 2 == 0 and nums[mid] == nums[mid + 1])):
        low = mid + 1
      else:
        high = mid
    return nums[low]
