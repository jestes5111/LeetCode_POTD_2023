class Solution:
  def restoreIpAddresses(self, s: str) -> List[str]:
    answer = []

    def backtrack(i: int, address: str) -> None:
      if i == len(s):
        if len(address) == 4: answer.append('.'.join(map(str, address)))
        return
    
      if address[-1] != 0 and address[-1] * 10 + int(s[i]) <= 255:
        last = address[-1]
        address[-1] = last * 10 + int(s[i])
        backtrack(i + 1, address)
        address[-1] = last

      if len(address) < 4:
        address.append(int(s[i]))
        backtrack(i + 1, address)
        address.pop()

    backtrack(1, [int(s[0])])
    return answer
