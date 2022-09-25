import pygame
import time

def BFSearch(initial):
  frontier = [initial]

  # print(frontier[0].board)
  explored = []
  while (len(frontier) != 0):
    currentState = frontier.pop()
    # print(currentState)
    # print(frontier)
    explored.append(currentState)
#     if (GoalTest(currentState)) return currentState
#     else:
#       for (Action a in Actions(currentState)):
#         if (Result(currentState, a) not in explored | frontier):
#           frontier.enqueue(Result(currentState, a))
  # print(frontier)
  # print(currentState)
  # print(explored)

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
    time.sleep(0.03)
    return x in range(self.x_pos, self.x_pos+100) and y in range(self.y_pos, self.y_pos+30)

def findEmptyCell(terminal_list):
  for i in range(3):
    for j in range(3):
      if terminal_list[i][j] == 0: # the neighboring cell is 0
        print(f"empty cell found: ({i}, {j})")
        return i, j

def clickedBfsDfs(screen, dfs, bfs, bfs_pink, dfs_pink, bfs_black, dfs_black):
  bfs.drawTile(screen, bfs_pink, bfs_black)
  dfs.drawTile(screen, dfs_pink, dfs_black)
