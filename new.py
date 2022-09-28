from operator import ne
import pygame
import time
from gameplay_functions import winnerCheck, swapCells, printArray

class Node:
  def __init__(self, board, empty_row, empty_column, action, parent):
    self.board = board
    self.empty_row = empty_row
    self.empty_column = empty_column
    self.action = action
    self.parent = parent

class Button:
  def __init__(self, x_pos, y_pos, name):
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.name = name

  def drawTile(self, screen, TILE_COLOR, FONT_COLOR):
    pygame.draw.rect(screen, TILE_COLOR, [self.x_pos, self.y_pos, 100, 30], 0, 15)

    font = pygame.font.Font('freesansbold.ttf', 15)
    screen.blit(font.render(self.name, True, FONT_COLOR), [(self.x_pos+self.x_pos+40)/2, (self.y_pos+self.y_pos+15)/2])

  def isClicked(self, x, y):
    time.sleep(0.05)
    return x in range(self.x_pos, self.x_pos+100) and y in range(self.y_pos, self.y_pos+30)

def findPath(currentState):
  actions_string_list = []
  while (currentState.parent):
    actions_string_list.insert(0, currentState.action)
    currentState = currentState.parent

  return actions_string_list, len(actions_string_list)

def copyBoard(currentStateBoard):
  new_board = []
  for i in range(3):
    row = []
    for j in range(3):
      row.append(currentStateBoard[i][j])
    new_board.append(row)

  return new_board
  

def Actions(currentState):
  action_list = []

  # for non-adjacent cells whose neighbor is 0
  new_board = copyBoard(currentState.board)
  i, j = findEmptyCell(new_board)

  try:
    if i-1 >= 0 and j >= 0:
      #swapping to UP
      print("====PARENT====")
      printArray(currentState.board)
      print("==============\n")
      print("=====CHILD=====")
      temp_board = swapCells(new_board, i, j, i-1, j)
      printArray(temp_board)
      print("===============\n")
  except IndexError:
    pass

  try:
    if i >= 0 and j >= 0:
      new_board = copyBoard(currentState.board)
      #swapping to UP
      print("====PARENT====")
      printArray(new_board)
      printArray(currentState.board)
      print("==============\n")
      print("=====CHILD=====")
      temp_board = swapCells(new_board, i, j, i, j+1)
      printArray(temp_board)
      print("===============\n")
  except IndexError:
    pass




  # newNode = swapping(currentState, -1, 0, "U")
  # action_list = addToActions(newNode, action_list)

  # newNode = swapping(currentState, 1, 0, "D")
  # action_list = addToActions(newNode, action_list)

  # newNode = swapping(currentState, 0, -1, "L")
  # action_list = addToActions(newNode, action_list)

  # newNode = swapping(currentState, 0, +1, "R")
  # action_list = addToActions(newNode, action_list)

  # print(len(action_list))
  # return action_list

def inExploredOrFrontier(node, explored):
  for item in explored:
    if node.board == item.board:
      return True
  return False

def BFS_DFS(initial):
  frontier = [initial]
  explored = []

  # while (frontier):
  currentState = frontier.pop(0)
    # printArray(currentState.board)
    # if None in frontier: frontier.remove(None)
  explored.append(currentState)
  if (winnerCheck(currentState.board)):
    print("Goal state achieved!")
    return currentState
  else:
    Actions(currentState)
      
    #   nodes_list = Actions(currentState)
    #   for item in nodes_list:
    #     if (not inExploredOrFrontier(item, explored) or not inExploredOrFrontier(item, frontier)):
    #       frontier.append(item)
    
    # print(f"Explored States: {len(explored)}")

def findEmptyCell(terminal_list):
  for i in range(3):
    for j in range(3):
      if terminal_list[i][j] == 0: # the neighboring cell is 0
        print(f"empty cell found: ({i}, {j})")
        return i, j

def fileWrite(actions_list):
  with open('puzzle.out', 'w') as f:
    f.writelines([f"{x} " for x in actions_list])

def readOutputFile():
  with open('puzzle.out', 'r') as file:
    data = file.read()
    return data

def clickedBfsDfs(screen, dfs, bfs, bfs_pink, dfs_pink, bfs_black, dfs_black):
  bfs.drawTile(screen, bfs_pink, bfs_black)
  dfs.drawTile(screen, dfs_pink, dfs_black)