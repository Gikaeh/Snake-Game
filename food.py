from random import randint

class Food:
    def __init__(self, MAP_WIDTH, MAP_HEIGHT, snake_body):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        self.snake_body = snake_body
        self.food = (0,0)

    def get_food(self):
        return self.food
    
    def set_food(self, n):
        self.food = n

    def place_food(self):
        food = (randint(1, self.width - 2), randint(1, self.height - 2))

        while food in self.snake_body:
            food = (randint(1, self.width - 2), randint(1, self.height - 2))

        return food

    def snake_hit_food(self, food_position, game):
        if food_position == self.snake_body[0]:
            food_position = self.place_food()
            game.set_eaten(True)

        return food_position
