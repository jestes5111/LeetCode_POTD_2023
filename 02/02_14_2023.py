class Solution:
  def addBinary(self, a: str, b: str) -> str:
    carry = 0
    answer = ''

    a, b = list(a), list(b)
    while a or b or carry:
      if a: carry += int(a.pop())
      if b: carry += int(b.pop())
      answer += str(carry % 2)
      carry //= 2
      
    return answer[::-1]
