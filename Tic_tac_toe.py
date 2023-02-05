import random
board = [' ' for x in range(9)]
''''
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |
'''
def print_board():
    print()
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print()

def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print(f"Your Turn Player {number}") 
    choice = int(input("Enter Your Move (1-9): ").strip())
    if board[choice-1] == " ":
        board[choice-1] = icon
    else:
        print("\nThat space is already taken!")

def computer_move(icon):
    while True:
        choice = random.randint(0,8)
        if board[choice-1] == " ":
            board[choice-1] = icon 
            break
 
def is_victory(icon):
    if ((board[0] == icon and board[1] == icon and board[2] == icon) or  
        (board[3] == icon and board[4] == icon and board[5] == icon) or 
        (board[6] == icon and board[7] == icon and board[8] == icon) or
        (board[0] == icon and board[3] == icon and board[6] == icon) or 
        (board[1] == icon and board[4] == icon and board[7] == icon) or 
        (board[2] == icon and board[5] == icon and board[8] == icon) or
        (board[0] == icon and board[4] == icon and board[8] == icon) or 
        (board[2] == icon and board[4] == icon and board[5] == icon) ):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move('X')
    print_board()
    if is_victory('X'):
        print("X wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw! ")
        break
    computer_move('O')
    if is_victory('O'):
        print("O wins! Congratulations!")
        break
    elif is_draw():
        print("It's a draw! ")
        break