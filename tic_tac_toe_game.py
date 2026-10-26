
while True:
  board=[['-','-','-'],['-','-','-'],['-','-','-']]
  turn="X"
  winning_list=[
      [(0,0), (0,1), (0,2)],   # top row
      [(1,0), (1,1), (1,2)],   # middle row
      [(2,0), (2,1), (2,2)],   # bottom row
      [(0,0), (1,0), (2,0)],   # left column
      [(0,1), (1,1), (2,1)],   # middle column
      [(0,2), (1,2), (2,2)],   # right column
      [(0,0), (1,1), (2,2)],   # main diagonal
      [(0,2), (1,1), (2,0)],
  ]

  def board_display():
    for index,item in enumerate(board):
      cells=[]
      for indexs,items in enumerate(item):
        if items == '-':
          cells.append(str(index*3+indexs+1))
        else:
          cells.append(items)
      print(" | ".join(cells))
      if index < 2:
        print("--+---+---")

  def player_win(turn):
        for index in winning_list:
          a,b,c=index
          if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] == turn :
            return True
        return False

  def draw():
    for row in board:
      for cell in row:
        if '-' in cell:
            return False
    return True

    
  while True:
    board_display()
    while True:
        try:
            move=int(input(f"player {turn} , pick a cell(1-9): "))
            if not (0< move < 10):
                print("enter value between 1 to 9")
                continue
            row=(move-1)//3
            col=(move-1) % 3
            if board[row][col] != '-': 
                
                print(f"{move} is already filled")
                continue
            break
        except ValueError:
          print("enter a number")
    board[row][col]=turn
    if player_win(turn):
      board_display()
      print(f"{turn} is win")
      break

    if draw():
      board_display()
      print("Draw")
      break


    if turn == "X":
      turn="O"
    else:
      turn="X"


  choice=input("play again(y/n):")
  if choice == "y":
      continue
  else:
      break






