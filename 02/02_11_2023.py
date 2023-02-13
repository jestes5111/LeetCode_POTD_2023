class Solution:
  def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
    graph = defaultdict(list)
    for a, b in redEdges: graph[a].append((b, "r"))
    for a, b in blueEdges: graph[a].append((b, "b"))

    answer = [-1] * n
    visited = set()
    queue = deque([(0, 0, None)])
    while queue:
      node, distance, previousEdge = queue.popleft()
      visited.add((node, previousEdge))
      if answer[node] == -1: answer[node] = distance

      for neighbor, edge in graph[node]:
        if (neighbor, edge) not in visited and previousEdge != edge:
          queue.append((neighbor, distance + 1, edge))
    
    return answer
