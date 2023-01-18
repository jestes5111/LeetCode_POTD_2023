class Solution:
  def maxSubarraySumCircular(self, nums: List[int]) -> int:
    if len(nums) == 1: return nums[0]

    sum_nums = sum(nums)
    answer = nums[0]
    max_subarray, min_subarray = nums[0], 0

    for i in range(1, len(nums)):
      max_subarray = max(max_subarray + nums[i], nums[i])
      min_subarray = min(min_subarray + nums[i], nums[i])
      answer = max(answer, max_subarray, sum_nums - min_subarray)
    return answer
