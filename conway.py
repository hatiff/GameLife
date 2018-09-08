# -*- coding: utf-8 -*-
import numpy as np
import sys

class Life():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.alive = 0
    
    #Create board   
    def Mboard(self):
        self.board = np.zeros((self.rows, self.columns))
        self.board[30, 50] = 1
        self.board[31, 51] = 1
        self.board[32, 49] = 1
        self.board[32, 50] = 1
        self.board[32, 51] = 1
       
    #Cycle of life 
    def cell(self):
        self.leav = self.board.copy() 
        self.new  = np.zeros((self.rows, self.columns))
        for row in range(self.rows):
            for column in range(self.columns):
                self.row = row
                self.column = column
                self.live()
                self.death()
        self.genesis()
                
    #Calculate the neighbors
    def neighbors(self):
        r = self.row
        c = self.column
        neighbors = 0
        nr1 = r + 1
        nr0 = r - 1
        nc1 = c + 1
        nc0 = c - 1
        if r == 0:
            nr1 = r + 1
            nr0 = -1
        elif r == self.rows - 1:
            nr1 = 0
            nr0 = r - 1
        
        if c == 0 :
            nc1 = c + 1
            nc0 = -1
        elif c == self.columns - 1:
            nc1 = 0
            nc0 = c - 1
        
        for row in [r, nr1, nr0]:
            for colm in [c, nc1, nc0]:
                neighbors += self.board[row, colm]    
        if self.board[r, c] == 1:
            neighbors -= 1      
        self.nei = neighbors 
            
    def live(self):
        self.neighbors()
        if self.nei == 3:
            if self.board[self.row, self.column] != 1:
                self.new[self.row, self.column] = 1
    
    def death(self):
        self.neighbors()
        if self.nei < 2 or self.nei > 3:
            self.leav[self.row, self.column] = 0
    
    def genesis(self):
        self.board = self.new + self.leav



