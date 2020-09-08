import pprint

# solver.py

def solve(board):

    """
    Sudoku solver using backtracking algorithm.
    :param: board = 2d list of integers
    :return: solution
    """

    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(board, pos, num):
    """
    Returns is the attempted move is valid
    :param board: 2d list of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """
    # Check Row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[1] != i:
            return False

    # Check Box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def find_empty(board):
    """
    Finds an empty space at the board
    :param: board: 2d list of ints
    :return: (int, int) row, col
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None


def print_sudoku(board):
    """
    Prints the game board
    :param: board: 2d list of ints
    :return: None
    """

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="\n")


board = [
        [2, 0, 0, 6, 0, 0, 8, 3, 0],
        [9, 0, 8, 5, 3, 0, 6, 0, 2],
        [0, 0, 1, 8, 0, 7, 0, 4, 0],
        [0, 6, 0, 0, 5, 3, 0, 0, 0],
        [7, 0, 4, 2, 0, 8, 0, 0, 0],
        [0, 2, 3, 4, 9, 6, 0, 0, 0],
        [0, 8, 0, 0, 6, 0, 0, 0, 5],
        [0, 0, 0, 1, 0, 5, 7, 6, 3],
        [5, 0, 6, 3, 0, 4, 0, 0, 0],
    ]   

pp = pprint.PrettyPrinter(width=41, compact=True)
solve(board)
pp.pprint(board)
