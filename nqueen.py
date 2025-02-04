# n queen problem:
# create a function to solve n-queen problem where n number of queens are placed in a n*n board where we have to avoid the queens clashing each other on the board


## the solution can be approached by avoiding two queens to be placed in same row, column or diagonal.

#take the 'n' number of queen

Q = int(input("Enter the number of queens: "))
print(f"There are {Q} queens")

##function to create board
def queenBoard(board, col):
    if col == Q:
        for row in board:
            print(row)
        print()  
        return True
    res = False
    for i in range(Q):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = queenBoard(board, col + 1) or res
            board[i][col] = 0
    return res

##function to check position of queens to avoid clashing
def isSafe(board, row, col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    for x, y in zip(range(row, Q, 1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    return True

board = [[0 for x in range(Q)] for y in range(Q)]

##if no solution is found
if not queenBoard(board, 0):
    print("Can't find any solution")
