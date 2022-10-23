# Num of places

board = [" " for i in range(9)]

# Creating the spaces
def print_board():
    row1 = "|{}||{}||{}|".format(board[0], board[1], board[2])
    row2 = "|{}||{}||{}|".format(board[3], board[4], board [5])
    row3 = "|{}||{}||{}|".format(board[6], board[7], board [8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
# num of players and what carecter they are operating.
def player_move(icon):
    if icon == "X":
        
        num = 1
    elif icon == "O":
        num = 2

    print("Your turn player {}".format(num))
    
# lincing players carecters to the icon, and asking for input, and lmiting the places 
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice -1] == " ":
        board[choice -1] = icon
    else:
        print()
        print("That space is taken!")
# determinating all the possible ways of victory
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or\
       (board[3] == icon and board[4] == icon and board[5] == icon) or\
       (board[6] == icon and board[7] == icon and board[8] == icon) or\
       (board[0] == icon and board[3] == icon and board[6] == icon) or\
       (board[1] == icon and board[4] == icon and board[7] == icon) or\
       (board[2] == icon and board[5] == icon and board[8] == icon) or\
       (board[0] == icon and board[4] == icon and board[8] == icon) or\
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
# No one wone a game \ no enough places for the game.
def is_draw():
    if " " not in board:
        return True
    else:
        return False
       

# making the game work till the end of all places
while True:
# declearing how the X player vins or no one wins    
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins! Congratulations!")
        break     
    elif is_draw():
        print("It is a draw!")
        break
# declearing how the O player vins or no one wins       
    player_move("O")
    if is_victory("O"):
         print_board()
         print("O wins! Congratulations!")
         break
    elif is_draw():

        print("It is a draw!")
        break
    
    
    
