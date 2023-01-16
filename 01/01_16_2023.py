class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    insertInterval = bisect_left(intervals, newInterval)
    intervals.insert(insertInterval, newInterval)

    i = 0
    while i < len(intervals):
      a, b = intervals[i]
      if i > 0 and intervals[i - 1][1] >= a:
        lastA, lastB = intervals[i - 1]
        intervals[(i - 1):(i + 1)] = [[lastA, max(lastB, b)]]
      else:
        i += 1
      
    return intervals
