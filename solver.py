board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    """
    Prints the board
    :return: None
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end ="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
        if (i+1) % 3 == 0 and i != 0 and i!= 8:
            print("----------------------")

def find_empty(bo):
    """
    Find the empty spots in one row
    :return: tuple
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) #row,col
    return None

def valid(num,row,col,bo):
    """
    Check the validation of the user's chosen number
    :param number: user's chosen number (int)
    :param row: current row (int)
    :param col: current column (int)
    :return: bool
    """
    row_check = bo[row]
    ii = 0
    #Check row
    for n,i in enumerate (row_check):
        if i != 0:
            if n == len(bo[0]) - 1:
                for ii in range (len(bo[0])):
                    if num == row_check[ii]:
                        return False
            else:
                if i == num:
                    return False
    #Check column
    for i in range (len(bo)):
        if num == bo[i][col] and row != i:
            return False
    #Check square
    box_x = col // 3
    box_y = row // 3

    for i in range (box_y*3, box_y*3 + 3):
        for j in range (box_x*3, box_x*3 + 3):
            if num == bo[i][j] and (i,j) != (row,col):
                return False    
    return True

def solve(bo):
    empty = find_empty(bo)
    if empty:
        row,col = empty 
    else:
        return True

    for i in range (1,10):
        if valid(i,row,col,bo):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
            
    return False

print_board(board)
solve(board)
print("___________________")
print_board(board)
