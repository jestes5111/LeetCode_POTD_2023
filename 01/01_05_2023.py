class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[1])

    arrows = 1
    bow = points[0][1]
    for start, end in points:
      if bow < start:
        bow = end
        arrows += 1

    return arrows
