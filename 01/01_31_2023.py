class Solution:
  def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
    if len(scores) == 1: return scores[0]

    team = [0] * (1 + max(ages))
    players = sorted(zip(scores, ages))
    for score, age in players:
      team[age] = score + max(team[:(age + 1)])
    return max(team)
