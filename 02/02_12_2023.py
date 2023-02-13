class Solution:
  def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
    graph = defaultdict(list)
    for x, y in roads:
      graph[x].append(y)
      graph[y].append(x)

    self.answer = 0

    def dfs(i: int, previous: int, people: int = 1) -> int:
      for x in graph[i]:
        if x == previous: continue
        people += dfs(x, i)
      self.answer += (int(ceil(people / seats)) if i else 0)
      return people

    dfs(0, 0)
    return self.answer
