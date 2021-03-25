#Project: Sudoku game
#Create on Sun March 22 2021
#Author: Duyen Bui
#Object Oriented Programming

import numpy as np

class board():

    def __init__(self,board):
        self.bo = np.array(board)
        self.size = len(self.bo)
        self.num = len(self.bo[0])

    def print_board(self):
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

    def find_spot(self):
        self.spot = []
        for i in range(self.size):
            for j in range(self.num):
                if self.bo[i][j] == 0:
                    self.spot.append([i,j])
    
    def fill_spot(self):
        self.empty = len(self.spot)
        ii = 0
        for j in range (self.empty):
            self.slot = self.spot[j]
            self.row = self.slot[0]
            self.col = self.slot[1]
            print("Please choose a number for row", str(self.row + 1) + " and column", str(self.col + 1) + ":")
            self.user = input()
            self.input_num = int(self.user)

            while (self.input_num > 9 or self.input_num <= 0):
                    self.user = input(("Oh no!!! Please choose another number from one to nine:"))
                    self.input_num = int(self.user)

            self.row_check = self.bo[self.row]

            if self.row != 0:
                for i in range (self.size):
                    if i != self.row:
                        while self.input_num == self.bo[i][self.col]:
                            self.user = input(("Oh no!!! Please choose another number:"))
                            self.input_num = int(self.user)
                            while (self.input_num > 9 or self.input_num <= 0):
                                self.user = input(("Oh no!!! Please choose another number from 1 to 9:"))
                                self.input_num = int(self.user)   
            elif self.row == 0:
               for i in range (self.size - 1):
                    while self.input_num == self.bo[i+1][self.col]:
                        self.user = input(("Oh no!!! Please choose another number:"))
                        self.input_num = int(self.user)  
                        while (self.input_num > 9 or self.input_num <= 0):
                            self.user = input(("Oh no!!! Please choose another number from 1 to 9:"))
                            self.input_num = int(self.user)  

            for n,i in enumerate(self.row_check):
                if n == self.num - 1:
                    for ii in range (self.num):
                        while self.input_num == self.row_check[ii]:
                            print('fish')
                            self.user = input(("Oh no!!! Please choose another number:"))
                            self.input_num = int(self.user)
                        while (self.input_num > 9 or self.input_num <= 0):
                            print('fish 1')
                            self.user = input(("Oh no!!! Please choose another number from 1 to 9:"))
                            self.input_num = int(self.user) 
                    self.row_check[self.col] = self.input_num
                    self.print_board()
                    print('fish 2')
                else:
                    while self.input_num == i:
                        self.user = input(("Oh no!!! Please choose another number:"))
                        self.input_num = int(self.user)  
                        print('fish 3')
                        while (self.input_num > 9 or self.input_num <= 0):
                            self.user = input(("Oh no!!! Please choose another number from 1 to 9:"))
                            self.input_num = int(self.user)                              
        print("Well done!!!")

if __name__ == "__main__":
    game = board([
    [7,8,9,2,0,0,0,3,6],
    [6,5,0,9,1,2,8,0,0],
    [0,5,0,0,7,0,0,9,8],
    [1,7,0,0,5,9,0,0,3],
    [5,0,0,8,0,0,1,6,0],
    [0,1,5,0,0,8,3,0,0],
    [0,0,4,1,0,0,6,8,0],
    [5,8,0,9,2,3,0,0,0],
    [0,0,2,1,0,0,6,0,4]
    ])
    game.print_board()
    game.find_spot()
    game.fill_spot()





