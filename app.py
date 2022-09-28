# Punzalan, Kurt Brian Daine B. Punzalan
# 2020-00772
# CMSC 170 X-4L
# Exer 01

import pygame
import time
from gameplay_functions import *
from settings import *
from bfs_dfs import *
import os

os.system('cls')

# MAIN FILE
terminal_list = []
terminal_list = readFile()

tiles_list = []
tiles_list = addTiles() 

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("8 Puzzle Game")
icon = pygame.image.load('./assets/jigsaw.png')
pygame.display.set_icon(icon)


font = pygame.font.Font('freesansbold.ttf', 20)
not_solvable, textRect = textDisplay(font, 'Puzzle is not Solvable!', RED, WIN_WIDTH, 150, 25)
won, textRect_won = textDisplay(font, 'You Win!', BLACK, WIN_WIDTH, 150, 25)

# if number of inversions is odd, it is not solvable
is_solvable = True
if not isSolvable(terminal_list):
  is_solvable = False

is_path_seen = False
is_next_running = False
is_playable = True
is_bfs_clicked = ""
to_be_solved = ""

is_running = True
while is_running:
  screen.fill(LIGHT)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      is_running = False

  # renders/reprints all tiles
  printTiles(tiles_list, terminal_list, screen, PINK_100, BLACK)
    
  # if number of inversions is odd, it is not solvable
  if not is_solvable:
    screen.blit(not_solvable, textRect)

  if winnerCheck(terminal_list):
    screen.blit(won, textRect_won)
    printTiles(tiles_list, terminal_list, screen, PINK_50, BLACK_50)
    is_playable = False # user will not be able to click anymore
    is_path_seen = False

  if is_path_seen:
    pathText, pathTextRect = textDisplay(font, f"Path Cost: {str(path_cost)}", BLACK, WIN_WIDTH, 150, 25)
    screen.blit(pathText, pathTextRect)

    path_list_text, path_list_rect = textDisplay(font, f"Path: {outputPath}", BLACK, WIN_WIDTH*2, WIN_HEIGHT*2, WIN_HEIGHT-50)
    screen.blit(path_list_text, path_list_rect)

  # BFS-DFS Specs
  solution = Button(400, 285, "Solution")
  solution.drawTile(screen, PINK_100, BLACK)

  bfs = Button(400, 50, "BFS")
  dfs = Button(400, 90, "DFS")
  clickedBfsDfs(screen, dfs, bfs, PINK_100, PINK_100, BLACK, BLACK)

  next = Button(400, 325, "Next")
  if (is_next_running):
    next.drawTile(screen, PINK_100, BLACK)

  if (is_bfs_clicked == "1"):
    clickedBfsDfs(screen, dfs, bfs, PINK_50, PINK_100, BLACK_50, BLACK)
  elif (is_bfs_clicked == "2"):
    clickedBfsDfs(screen, dfs, bfs, PINK_100, PINK_50, BLACK, BLACK_50)

  # GAMEPLAY
  if event.type == pygame.MOUSEBUTTONDOWN:
    try:
      x, y = pygame.mouse.get_pos()
      
      if next.isClicked(x, y):
        if (currentState):
          i, j = findEmpty(terminal_list)

          match actions_string_list[actions_index]:
            case "L": terminal_list = swapCells(terminal_list, i, j, i, j-1)
            case "R": terminal_list = swapCells(terminal_list, i, j, i, j+1)
            case "U": terminal_list = swapCells(terminal_list, i, j, i-1, j)
            case "D": terminal_list = swapCells(terminal_list, i, j, i+1, j)

        actions_index += 1


      if (x <= 400): # tiles are being checked/played
        row_clicked, col_clicked = calculateCoordinate(tiles_list, x, y)

        printArray(terminal_list)

        if is_playable:
          if terminal_list[row_clicked][col_clicked] == 0:
            print("You cannot click this cell")
          else:
            gameplay(terminal_list, row_clicked, col_clicked)
      else: # specification for BFS and DFS
        if (dfs.isClicked(x, y)):
          is_bfs_clicked = "2"
          print(f"Checking for the solution using {dfs.name}")
          to_be_solved = "dfs"

        elif (bfs.isClicked(x, y)):
          is_bfs_clicked = "1"
          print(f"Checking for the solution using {bfs.name}")
          to_be_solved = "bfs"

        if (solution.isClicked(x, y) and (to_be_solved == "bfs" or to_be_solved == "dfs")):
            is_playable = False

            terminal_list = readFile()

            if not isSolvable(terminal_list):
              print("Puzzle is Not Solvable!")
            else:
              print(f"Solution for {to_be_solved}")
              is_next_running = True

              i, j = findEmptyCell(terminal_list)
              initial = Node(terminal_list, i, j, None, None)
              
              if (to_be_solved == "bfs"):
                currentState = BFS_DFS(initial)
              else:
                currentState = BFS_DFS(initial)

              actions_string_list, path_cost = findPath(currentState)
              actions_index = 0
              print(actions_string_list)
              fileWrite(actions_string_list)
              is_path_seen = True

              outputPath = readOutputFile()

    except TypeError:
      print("This area cannot be clicked")
  # time.sleep(0.03)
  pygame.display.update()
  
pygame.quit()