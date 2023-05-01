from random import randint

class Food:
    def __init__(self, MAP_WIDTH, MAP_HEIGHT, snake_body):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        self.snake_body = snake_body

    def place_food(self):
        new_food = (randint(1, self.width - 2), randint(1, self.height - 2))

        while new_food in self.snake_body:
            new_food = (randint(1, self.width - 2), randint(1, self.height - 2))

        return new_food

    def snake_hit_food(self, food_position, eaten):
        if food_position == self.snake_body[0]:
            food_position = self.place_food()
            eaten = True

        return food_position, eaten
