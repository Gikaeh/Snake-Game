from pytimedinput import timedInput
from platform import system
import os
from random import randint

class Game:
    def __init__(self, MAP_WIDTH, MAP_HEIGHT):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        self.eaten = False
        self.boxes = [(col, row) for row in range(self.height) for col in range(self.width)]

    def show_field(self, snake_body, food_position):
        for box in self.boxes:
            if box in snake_body:
                print('O', end='')
            elif box[0] in (0, self.width - 1) or box[1] in (0, self.height - 1):
                print('#', end='')
            elif box == food_position:
                print('$', end='')
            else:
                print(' ', end='')

            if box[0] == self.width - 1:
                print('')

    def play_game(self, snake, food, food_position):
        while True:
            if system == 'Windows':
                os.system('cls')
            else:
                os.system('clear')

            self.show_field(snake.body, food_position)

            txt, _ = timedInput('get input:', timeout=.4)
            match txt:
                case 'w':
                    snake.direction = snake.directions['up']
                case 'a':
                    snake.direction = snake.directions['left']
                case 's':
                    snake.direction = snake.directions['down']
                case 'd':
                    snake.direction = snake.directions['right']

            self.eaten = snake.update_snake(self.eaten)
            food_position, self.eaten = food.snake_hit_food(food_position, self.eaten)

            end = self.check_death(snake)
            if end:
                break


    def check_death(self, snake):
        if snake.body[0][0] in (0, self.width-1) or snake.body[0][1] in (0, self.height-1) or snake.body[0] in snake.body[1:]:
            if system == 'Windows':
                os.system('cls')
            else:
                os.system('clear')
            
            return True