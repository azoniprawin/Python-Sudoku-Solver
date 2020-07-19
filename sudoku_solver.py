def display_board(board):
    for i in range(9):
        if(i%3 == 0):
            print("-" * 25)
        for j in range(9):
            if(j%3 == 0):
                print(end="| ")
            print(board[i][j], end=" ")
        print("|")
    print("-" * 25, "\n")

def find_empty_position(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                return i,j
    return False

def is_valid(board, number, position):
    for i in range(9):
        if(board[position[0]][i] == number):
            return False
    for i in range(9):
        if(board[i][position[1]] == number):
            return False
    x, y = (position[1]//3)*3, (position[0]//3)*3
    for i in range(3):
        for j in range(3):
            if(board[y+i][x+j] == number):
                return False
    return True

def solve(board):
    position = find_empty_position(board)
    if(position == False):
        return True
    for number in range(1, 10):
        if(is_valid(board, number, position)):
            board[position[0]][position[1]] = number
            if(solve(board)):
                return True
            board[position[0]][position[1]] = 0
    return False

board = [
    [2,0,0,3,0,0,0,0,0],
    [8,0,4,0,6,2,0,0,3],
    [0,1,3,8,0,0,2,0,0],
    [0,0,0,0,2,0,3,9,0],
    [5,0,7,0,0,0,6,2,1],
    [0,3,2,0,0,6,0,0,0],
    [0,2,0,0,0,9,1,4,0],
    [6,0,1,2,5,0,8,0,9],
    [0,0,0,0,0,1,0,0,2]
]

display_board(board)
solve(board)
display_board(board)
