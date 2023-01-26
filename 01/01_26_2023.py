class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adjacents = {i:[] for i in range(n)}
    for start, end, price in flights:
      adjacents[start].append((end, price))

    visited = [2 ** 31] * n
    queue = [(0, -1, src)]

    while queue:
      cost, steps, node = heapq.heappop(queue)
      if visited[node] <= steps: continue
      if steps > k: continue
      if node == dst: return cost

      visited[node] = steps
      for neighbor, weight in adjacents[node]:
        heapq.heappush(queue, (cost + weight, steps + 1, neighbor))

    return -1
