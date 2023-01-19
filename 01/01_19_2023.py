class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    frequency = defaultdict(int)
    frequency[0] = 1

    answer = prefix_sum = 0
    for num in nums:
      prefix_sum += num
      remainder = prefix_sum % k
      answer +=  frequency[remainder]
      frequency[remainder] += 1
    return answer
