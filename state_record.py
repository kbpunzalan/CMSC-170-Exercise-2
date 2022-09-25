# typedef struct state_record {
# int *puzzle; 
# int empty_loc; // 
# char action; // char 
# struct state_record *parent; // 
# }NODE;

class StateRecord():
  def __init__(self, puzzle, empty_loc, action, parent):
    self.puzzle = puzzle # (array of integers) array containing the tile values
    self.empty_loc = empty_loc # index of the empty tile
    self.action = action # action to arrive at this state
    self.parent = parent # a pointer to the parent node