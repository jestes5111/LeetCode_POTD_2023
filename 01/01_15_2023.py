class Solution:
  def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
    adjacents = {}

    def find (x: int) -> int:
      adjacents.setdefault(x, x)
      if x != adjacents[x]:
        adjacents[x] = find(adjacents[x])
      return adjacents[x]
    
    def union(x: int, y: int) -> None:
      adjacents[find(x)] = find(y)

    tree = defaultdict(list)
    nodes = defaultdict(set)
    for a, b in edges:
      tree[a].append(b)
      tree[b].append(a)
      nodes[vals[a]].add(a)
      nodes[vals[b]].add(b)
    
    answer = len(vals)

    for value in sorted(nodes.keys()):
      for node in nodes[value]:
        for neighbor in tree[node]:
          if vals[neighbor] <= value: 
            union(node, neighbor)
    
      count = defaultdict(int)
      for node in nodes[value]:
        count[find(node)] += 1
      
      for root in count.keys():
        answer += comb(count[root], 2)

    return answer
