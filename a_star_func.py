from gameplay_functions import winnerCheck
from bfs_dfs import inExploredOrFrontier

def findCellBeingChecked(number_checked):
  newBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
  for i in range(3):
    for j in range(3):
      if newBoard[i][j] == number_checked:
        return i, j

def computeH(initial_board):
  total = 0
  for i in range(3):
    for j in range(3):
      if initial_board[i][j] == 0:
        continue
      correct_row, correct_column = findCellBeingChecked(initial_board[i][j])
      
      distance = abs(i - correct_row) + abs(j - correct_column)
      total += distance

  return total
  # print(total)

def removeMinF(openList):
  pass

def AStar(initial):
  openList = [initial] # same as frontier
  closedList = [] # same as explored
  
  computeH(initial.board)

  # while(openList):
  #   bestNode = removeMinF(openList)
  #   print(f"Explored States: {len(closedList)}")
  #   if (winnerCheck(bestNode.board)):
  #     print("Goal state achieved!")
  #     return bestNode
  #   for a in Actions(bestNode):
  #     x = Result(bestNode, a)
  #     if (not inExploredOrFrontier(item, openList) and not inExploredOrFrontier(item, closedList)) or (inExploredOrFrontier(item, openList) and x.g < duplicate.g):
  #       x.setParent(bestNode)
  #       openList.append(x)
