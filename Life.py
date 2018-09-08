import pygame
from pygame.locals import *
import numpy as np
from conway import Life

class GameOfLife(Life):
    def __init__(self, width = 1440, height = 960, cell_size = 10, speed = 10):
        Life.__init__(self, width // 10, height // 10)
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed
        self.Mboard()


    def draw_grid(self):
        
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))
            
    def cells(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.board[row, column] == 1:
                    pygame.draw.rect(self.screen, (57, 255, 20), ((row * 10) + 1, (column * 10) +1, self.cell_size -1, 
                                     self.cell_size -1))
                else:
                    pygame.draw.rect(self.screen, (255, 255, 255), ((row * 10) + 1, (column * 10) + 1, self.cell_size -1, 
                                     self.cell_size -1))
                    

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.cells()
            self.cell()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()


if __name__ == '__main__':
    game = GameOfLife()
    game.run()