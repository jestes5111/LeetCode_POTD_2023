class Solution:
  def maxIceCream(self, costs: List[int], coins: int) -> int:
    costs.sort()
    total = 0
    for cost in costs:
      if cost > coins:
        break
      coins -= cost
      total += 1
    return total
