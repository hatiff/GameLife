# -*- coding: utf-8 -*-
import numpy as np
import sys

class Life():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.alive = 0
        self.Cycle
       
    def Cycle(self):
        self.Mboard
        if self.alive == 0:
            self.end
        self.cell
        
    def Mboard(self):
        self.board = np.zeros(self.rows, self.columns)
        for row in self.rows:
            for column in self.columns:
                self.board[row, column] = np.random.randint(0, 1)
        self.alive = self.board.sum()

    def cell(self):
        for row in self.rows:
            for column in self.columns:
                self.row = row
                self.column = column
                self.neigbors
                self.death
                self.live
                
    
    def neighbor(self):
        r = self.row
        c = self.column
        neighbors = 0
        nr1 = r + 1
        nr0 = r - 1
        nc1 = c + 1
        nc0 = c - 1
        if r == 0:
            nr1 = r + 1
            nr0 = -r + 1
        elif r == self.rows - 1:
            nr1 = 0
            nr0 = r - 1
        
        if c == 0 :
            nc1 = c + 1
            nc0 = -c + 1
        elif c == self.columns - 1:
            nc1 = 0
            nc0 = c - 1
        
        for row in [r, nr1, nr0]:
            for colm in [c, nc1, nc0]:
                neighbors += self.board[row, colm]    
        if self.board[r, c] == 1:
            neighbors -= 1      
        self.nei = neighbors        
    
    def death(self):
        if self.nei < 2 or self.nei > 3:
            if self.board[self.row, self.column] == 1:
                self.alive -= 1
            self.board[self.row, self.column] = 0

            
    def live(self):
        if self.nei == 3:
            self.board[self.row, self.column] = 1
            self.alive += 1
    def end(self):
        sys.exit(1)

c = Life(1000, 1500)
print(c.alive)
