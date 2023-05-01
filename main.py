from game import Game
from snake import Snake
from food import Food

def main():
    MAP_WIDTH = 32
    MAP_HEIGHT = 16

    game = Game(MAP_WIDTH, MAP_HEIGHT)
    snake = Snake(MAP_HEIGHT)
    food = Food(MAP_WIDTH, MAP_HEIGHT, snake.body)

    food_position = food.place_food()

    game.play_game(snake, food, food_position)

if __name__ == "__main__":
    main()
        