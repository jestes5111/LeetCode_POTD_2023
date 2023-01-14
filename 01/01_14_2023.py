class Solution:
  def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    chars = {}

    def find(x: str) -> str:
      chars.setdefault(x, x)
      if x != chars[x]: 
        chars[x] = find(chars[x])
      return chars[x]

    def union(x: str, y: str) -> None:
      root_x, root_y = find(x), find(y)
      if root_x > root_y:
        chars[root_x] = root_y
      else:
        chars[root_y] = root_x
    
    for i in range(len(s1)):
      union(s1[i], s2[i])

    answer = []
    for char in baseStr:
      answer.append(find(char))

    return ''.join(answer)
