import unittest
from game import Game
from snake import Snake
from food import Food

class TestGameFunctions(unittest.TestCase):
    def setUp(self):
        self.game = Game(10, 10)
        #self.game3 = Game(10000, 10000)

    def test_game_width(self):
        self.assertEqual(self.game.get_width(), 10)

        self.game.set_width(0)
        self.assertEqual(self.game.get_width(), 0)
        #self.assertEqual(self.game3.width, 1000000)

    def test_game_height(self):
        self.assertEqual(self.game.get_height(), 10)

        self.game.set_height(0)
        self.assertEqual(self.game.get_height(), 0)

    def test_if_eaten(self):
        self.assertFalse(self.game.get_eaten())
        
        self.game.set_eaten(True)
        self.assertTrue(self.game.get_eaten())

class TestSnakeFunctions(unittest.TestCase):
    def setUp(self):
        self.snake = Snake(10)
        self.testDict = [(2,0), (1,0), (0,0)]

    def test_snake_body(self):
        self.snakeBody = self.snake.get_snake_body()
        self.assertEqual(self.snakeBody[0], (5,5))
        self.assertEqual(self.snakeBody[1], (4,5))
        self.assertEqual(self.snakeBody[2], (3,5))

        self.snake.set_snake_body(self.testDict)
        self.snakeBody = self.snake.get_snake_body()
        self.assertEqual(self.snakeBody[0], (2,0))
        self.assertEqual(self.snakeBody[1], (1,0))
        self.assertEqual(self.snakeBody[2], (0,0))

    def test_body_count(self):
        self.assertEqual(self.snake.get_body_count(), 3)

        self.snake.set_body_count(10000)
        self.assertEqual(self.snake.get_body_count(), 10000)

        self.snake.set_body_count(0)
        self.assertEqual(self.snake.get_body_count(), 0)

class TestFoodFunctions(unittest.TestCase):
    def setUp(self):
        self.food = Food(10, 10, [(5,5), (4,5), (3,5)])

    def test_food(self):
        self.assertEqual(self.food.get_food(), [0,0])

        self.food.set_food([1,5])
        self.assertEqual(self.food.get_food(), [1,5])

if __name__ == '__main__':
    unittest.main()