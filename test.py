import unittest
from game import Game
from snake import Snake
from food import Food

class TestUnitFunctions(unittest.TestCase):
    def setUp(self):
        self.game = Game(10, 10)

        self.snake = Snake(10)
        self.testDict = [(2,0), (1,0), (0,0)]

        self.food = Food(10, 10, [(5,5), (4,5), (3,5)])

    def test_game_width(self):
        self.assertEqual(self.game.get_width(), 10)

        self.game.set_width(0)
        self.assertEqual(self.game.get_width(), 0)

    def test_game_height(self):
        self.assertEqual(self.game.get_height(), 10)

        self.game.set_height(0)
        self.assertEqual(self.game.get_height(), 0)

    def test_if_eaten(self):
        self.assertFalse(self.game.get_eaten())
        
        self.game.set_eaten(True)
        self.assertTrue(self.game.get_eaten())

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

    def test_food(self):
        self.assertEqual(self.food.get_food(), (0,0))

        self.food.set_food((1,5))
        self.assertEqual(self.food.get_food(), (1,5))

class TestIntegrationFunctions(unittest.TestCase):
    def setUp(self):
        self.game = Game(20, 20)

        self.snake = Snake(20)
        self.snake_inside = Snake(20, [(5,3),(4,2),(3,2),(5,3)])
        self.snake_wall = Snake(20, [(19,5),(18,5),(17,5)])

        self.food = Food(20, 20, self.snake.get_snake_body())

    def test_check_death(self):
        self.assertFalse(self.game.check_death(self.snake))
        self.assertTrue(self.game.check_death(self.snake_inside))
        self.assertTrue(self.game.check_death(self.snake_wall))

    def test_update_snake(self):
        self.assertEqual(self.snake.update_snake(self.game), 3)

        self.game.set_eaten(True)
        self.assertEqual(self.snake.update_snake(self.game), 4)

    def test_snake_hit_food(self):
        self.assertEqual(self.food.snake_hit_food(self.food.get_food(), self.game), (0,0))
        
        self.food.set_food((5,10))
        self.assertNotEqual(self.food.snake_hit_food(self.food.get_food(), self.game), (5,10))

    # def test_show_field(self):
    #     self.assertTrue(self.game.show_field(self.snake.get_snake_body(), self.food.get_food()))

    # def test_play_game(self):
    #     self.assertTrue(self.game.play_game(self.snake, self.food, self.food.get_food()))

if __name__ == '__main__':
    unittest.main()
