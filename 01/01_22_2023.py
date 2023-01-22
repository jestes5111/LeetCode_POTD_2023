class Solution:
  def partition(self, s: str) -> List[List[str]]:
    answer = []

    def is_palindrome(a: str) -> bool:
      return a == a[::-1]

    def dfs(i: int, current: str) -> None:
      if i == len(s): 
        answer.append(current)
        return
      for j in range(i, len(s)):
        temp = s[i:(j + 1)]
        if is_palindrome(temp):
          dfs(j + 1, current + [temp])
      return

    dfs(0, [])
    return answer
