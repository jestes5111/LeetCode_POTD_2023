# SOLVED MOSTLY ON MY OWN - NEEDED TO USE TWO `for` LOOPS
#     INSTEAD OF A ONELINER
class Solution:
  def minDeletionSize(self, strs: List[str]) -> int:
    columns_to_delete = 0

    # # PART I HAD INITIALLY
    # for i in range(len(strs)):
    #   column = [j[i] for j in strs]
    # # END INITIAL PART

    # PART I ENDED WITH
    for i in range(len(strs[0])):
      column = ''
      for j in range(len(strs)):
        column += strs[j][i]
    # END PART
      
      if ''.join(sorted(column)) != ''.join(column):
        columns_to_delete += 1
    
    return columns_to_delete