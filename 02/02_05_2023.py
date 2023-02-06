class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    window, string = len(p), len(s)
    answer = []
    if window > string: return answer

    wanted = [0] * 26
    for letter in p:
      wanted[ord(letter) - 97] += 1

    current = [0] * 26
    for i in range(window):
      current[ord(s[i]) - 97] += 1
    if current == wanted: answer.append(0)

    for i in range(window, string):
      current[ord(s[i - window]) - 97] -= 1
      current[ord(s[i]) - 97] += 1
      if current == wanted: answer.append(i + 1 - window)
    
    return answer
