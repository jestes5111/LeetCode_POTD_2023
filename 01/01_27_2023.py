class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    memory = {}
    words = set(words)

    def dfs(word: str) -> bool:
      if word in memory: return memory[word]

      for index in range(1, len(word)):
        prefix, suffix = word[:index], word[index:]
        if prefix in words and (suffix in words or dfs(suffix)): return True
      return False
      
    return [word for word in words if dfs(word)]
