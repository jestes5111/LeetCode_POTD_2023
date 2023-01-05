# NEEDED A BIT OF HELP
class Solution:
  def minimumRounds(self, tasks: List[int]) -> int:
    if len(tasks) == 1:
      return -1
    
    # NEEDED HELP HERE, `for` LOOP WAS TOO SLOW
    difficulties = Counter(tasks).values()

    rounds = 0
    for difficulty in difficulties:
      if difficulty == 1:
        return -1
      elif difficulty == 2 or difficulty == 3:
        rounds += 1
      else:
        # NEEDED CONCEPTUAL HELP HERE - EASIER TO DO MATHEMATICALLY
        #     THAN WITH LISTS
        rounds += (difficulty + 2) // 3
    return rounds