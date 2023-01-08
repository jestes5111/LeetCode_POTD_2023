class Solution:
  def maxPoints(self, points: List[List[int]]) -> int:
    points.sort()
    slope = defaultdict(int)
    answer = 0

    for i, (x1, y1) in enumerate(points):
      slope.clear()
      for x2, y2 in points[i + 1:]:
        dx = x2 - x1
        dy = y2 - y1

        temp = gcd(dx, dy)
        m = (dx // temp, dy // temp)

        slope[m] += 1
        if slope[m] > answer: answer = slope[m]

    return answer + 1
