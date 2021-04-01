#Project: Sudoku game
#Create on Sun March 22 2021
#Author: Duyen Bui
#Object Oriented Programming

import numpy as np

class board():

    def __init__(self,board):
        """
        Initialize Sudoku board
        :param board: 2d List of int
        :return: array of the the 2d list
                 size of matrix (int)
                 the number of the number in one row (int)
        """
        self.bo = np.array(board)
        self.size = len(self.bo)
        self.num = len(self.bo[0])

    def print_board(self):
        """
        Prints the board
        :return: None
        """
        for i in range(self.size):
            for j in range(self.num):
                if j % 3 == 0 and j != 0:
                    print("| ", end ="")

                if j == 8:
                    print(self.bo[i][j])
                else:
                    print(str(self.bo[i][j]) + " ", end="")
            if (i+1) % 3 == 0 and i != 0 and i!= 8:
                print("----------------------")

    def find_empty(self):
        """
        Find the empty spots in one row
        :return: 2d List of lists
        """
        self.empty = []
        for i in range(self.size):
            for j in range(self.num):
                if self.bo[i][j] == 0:
                    self.empty.append([i,j])

    def valid(self,number,row,col):
        """
        Check the validation of the user's chosen number
        :param number: user's chosen number (int)
        :param row: current row (int)
        :param col: current column (int)
        :return: bool
        """
        ii = 0
        self.number = number
        self.row = row
        self.col = col
        self.row_check = self.bo[self.row]
        #Check the value of number
        if self.number > 9 or self.number < 0:
            return False
        #Check row
        for n,i in enumerate (self.row_check):
            if i != 0:
                if self.num == n and self.col != i:
                    return False
                if n == self.num - 1:
                    for ii in range (self.num):
                        if self.number == self.row_check[ii]:
                            return False
                else:
                    if self.number == i:
                        return False
        #Check column
        for i in range (self.size):
            if self.number == self.bo[i][self.col] and self.row != i:
                return False
        #Check square
        self.box_x = self.col // 3
        self.box_y = self.row // 3

        for i in range (self.box_y*3, self.box_y*3 + 3):
            for j in range (self.box_x*3, self.box_x*3 + 3):
                if self.number == self.bo[i][j] and (i,j) != (row,col):
                    return False    
        return True

    def solve(self):
        """
        Solve the board, run a loop until reach the final pos
        :return: solved board(2d List of ints)
        """
        for ii in range (len(self.empty)):
            self.pos = self.empty[ii]
            self.row = self.pos[0]
            self.col = self.pos[1]
            print("Please choose a number for row", str(self.row + 1) + " and column", str(self.col + 1) + ":")
            self.user = input()
            self.input_num = int(self.user)
            if self.valid(self.input_num,self.row,self.col):
                self.bo[self.row][self.col] = self.input_num
                self.print_board()
            else:
                self.find_empty()  #restart the process
                self.solve()



if __name__ == "__main__":
    game = board([
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ])
    game.print_board()
    game.find_empty()
    game.solve()







