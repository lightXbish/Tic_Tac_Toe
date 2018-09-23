game_board = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

over = False


def display_board():
    for j in game_board:
        for i in j:
            if i == 0:
                print('|.| ', end='')
            elif i == 1:
                print('|x| ', end='')
            elif i == 2:
                print('|o| ', end='')
        print()


def opponent_player(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1


def position(player):
    print('Player ' + str(player) + "'s turn!!")
    row = int(input("Enter the Row: "))
    col = int(input("Enter the Column: "))
    while True:
        if row > 3 or row <= 0 or col > 3 or col <= 0:
            row = int(input("Enter the Row: "))
            col = int(input("Enter the Column: "))
        elif game_board[row - 1][col - 1] != 0:
            row = int(input("Enter the Row: "))
            col = int(input("Enter the Column: "))
        else:
            row -= 1
            col -= 1
            if player == 1:
                game_board[row][col] = 1
            elif player == 2:
                game_board[row][col] = 2
            display_board()
            break


def check_win():
    global over
    for i in range(0, 3):
        if game_board[i][0] == game_board[i][1] == game_board[i][2]:
            if game_board[i][0] == 1:
                print("Player 1 WINS !")
                print("GAME OVER !")
                over = True
                break
            elif game_board[i][0] == 2:
                print("Player 2 WINS !")
                print("GAME OVER !")
                over = True
                break
        elif game_board[0][i] == game_board[1][i] == game_board[2][i]:
            if game_board[0][i] == 1:
                print("Player 1 WINS !")
                print("GAME OVER !")
                over = True
                break
            elif game_board[0][i] == 2:
                print("Player 2 WINS !")
                print("GAME OVER !")
                over = True
                break

    if game_board[0][0] == game_board[1][1] == game_board[2][2] or game_board[0][2] == game_board[1][1] == \
            game_board[2][0]:
        if game_board[1][1] == 1:
            print('Player 1 WINS !')
            print("GAME OVER !")
            over = True
        elif game_board[1][1] == 2:
            print('Player 1 WINS !')
            print("GAME OVER !")
            over = True


def tic_tac_toe():
    global over
    player = 1
    display_board()
    opponent_player(player)
    count = 1
    while count < 10:
        position(player)
        opponent_player(player)
        player = opponent_player(player)
        check_win()
        if over == True:
            break
        count += 1
    print("Its a Draw !")
    print("Game Over !")


tic_tac_toe()
