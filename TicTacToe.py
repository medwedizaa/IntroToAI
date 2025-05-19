def get_user_input():
    x, y = input("Input move in ").split(" ")
    return int(x), int(y)


def print_board(b):
    print(" " + b[0][0] + " | " + b[0][1] + " | " + b[0][2] + " ")
    print("-----------")
    print(" " + b[1][0] + " | " + b[1][1] + " | " + b[1][2] + " ")
    print("-----------")
    print(" " + b[2][0] + " | " + b[2][1] + " | " + b[2][2] + " ")


def check_for_win_condition(b):
    for k in range(3):
        if b[k][0] == b[k][1] and b[k][1] == b[k][2] and b[k][1] != "":
            return b[k][1]
    for k in range(3):
        if b[0][k] == b[1][k] and b[1][1] == b[2][2] and b[1][1] != "":
            return b[1][i]
    if b[0][0] == b[1][1] and b[1][1] == b[2][2] and b[1][1] != "":
        return board[1][1]
    if b[0][2] == b[1][1] and b[1][1] == b[2][0] and b[1][1] != "":
        return b[1][1]
    return None


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]


run = True
user = 0
while run:
    while True:
        i, j = get_user_input()
        if -1 < i < 3 and -1 < j < 3:
            if board[i][j] == " ":
                break
            else:
                print("Illegal move, try again")
        else:
            print("Illegal move, try again")
    if user:
        board[i][j] = "X"
    else:
        board[i][j] = "0"

    user = not user
    print_board(board)
    if check_for_win_condition(board) == "X":
        print("X - winner")
        break
    if check_for_win_condition(board) == "0":
        print("0 - winner")
        break

    game_over = True
    for i in board:
        for j in i:
            if j == " ":
                game_over = False

    run = not game_over
print("Game over!")