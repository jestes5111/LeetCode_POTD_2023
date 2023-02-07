class Solution:
  def totalFruit(self, fruits: List[int]) -> int:
    if len(set(fruits)) < 3: return len(fruits)

    basket = {}
    start = end = maxVal = 0
    while end < len(fruits):
      basket[fruits[end]] = end
      if len(basket) >= 3:
        minVal = min(basket.values())
        del basket[fruits[minVal]]
        start = minVal + 1
      
      maxVal = max(maxVal, end - start + 1)
      end += 1
    return maxVal
