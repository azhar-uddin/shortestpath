board = []
distance=0

for x in range(12):
  board.append(["."] * 12)

def print_board(board):
  for row in board:
    print "   ".join(row)

def take_position_values(input):
  print "Enter the {}".format(input)
  while True:
    try:
      r = int(raw_input(input+str(" row: ")))
      c = int(raw_input(input+str(" col: ")))
    except ValueError:
      print "Kindly Enter a valid Input"
      continue
    else:
      if (not 0 <= r <= 11) or (not 0 <= c <= 11) or board[r][c] == "X":
        print "Kindly Enter a valid Position"
        continue
      else:
        return [r,c]
      break

def find_neighbours(row, column):
  neighbour_positions = []
  row_limit = 11
  if row_limit > 0:
    column_limit = 11
    x =  max(0, row-1)
    while x <= min(row+1, 11):
      y = max(0, column-1)
      while y <= min(column+1, 11):
        if(x != row or y!= column):
          neighbour_positions.append([x,y])
        y+=1
      x+=1
  return neighbour_positions

def next_step(row, column):
  new_positions = []
  neighbours = find_neighbours(row, column)
  for neighbour in neighbours:
    if board[neighbour[0]][neighbour[1]] == ".":
      board[neighbour[0]][neighbour[1]] = str(distance)
      new_positions.append(neighbour)
    elif board[neighbour[0]][neighbour[1]] == "D":
      new_positions.append(neighbour)
  return new_positions

def move_next_step(positions):
  next_positions = []
  for current_position in positions:
    if board[current_position[0]][current_position[1]] == "D":
      break
    next_positions.extend(next_step(current_position[0], current_position[1]))
  else:
    return next_positions
  return "Reached Destination"

def previous_step(row, column, dist):
  neighbours = find_neighbours(row, column)
  for neighbour in neighbours:
    if board[neighbour[0]][neighbour[1]] == str(dist-1):
      board[neighbour[0]][neighbour[1]] = "*"
      return neighbour

def find_path(row, column, dist):
  prev_step = [row,column]
  while(dist >0):
    prev_step = previous_step(prev_step[0], prev_step[1], dist)
    dist-=1

print_board(board)

print "Enter the number of Obstacles"
while True:
  try:
    obstacles = int(raw_input("number of obstacles: "))
  except ValueError:
    print "Kindly Enter a valid Input"
    continue
  else:
    break

for obstacle  in range(obstacles):
  print "Obstacle", obstacle + 1
  obstacle = take_position_values("obstacle")
  board[obstacle[0]][obstacle[1]] = "X"

print_board(board)

source = take_position_values("source")
board[source[0]][source[1]] = "S"
destination = take_position_values("destination")
board[destination[0]][destination[1]] = "D"

print_board(board)

current_positions = [[source[0], source[1]]]
while(isinstance(current_positions, basestring) == False):
  distance+=1
  current_positions = move_next_step(current_positions)

print "The shortest path is:"
print str(distance-1) + " Steps"
find_path(destination[0], destination[1], distance-1)
print_board(board)