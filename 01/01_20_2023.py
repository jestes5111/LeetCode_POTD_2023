class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    answer = set()

    def backtrack(i: int, subsequence: List[int]) -> None:
      nonlocal answer

      if len(subsequence) > 1: answer.add(tuple(subsequence))
      if i == len(nums): return
      
      if not subsequence or nums[i] >= subsequence[-1]:
        backtrack(i + 1, subsequence + [nums[i]])
      backtrack(i + 1, subsequence)
    
    backtrack(0, [])
    return answer
