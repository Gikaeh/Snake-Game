import unittest
from game import Game
from snake import Snake
from food import Food

class TestIntegrationFunctions(unittest.TestCase):
    def setUp(self):
        self.game = Game(20, 20)
        self.snake = Snake(20)
        self.snake_inside = Snake(20, [(5,3),(4,2),(3,2),(5,3)])
        self.snake_wall = Snake(20, [(19,5),(18,5),(17,5)])
        self.food = Food(20, 20, self.snake)

    def test_check_death(self):
        self.assertFalse(self.game.check_death(self.snake))
        self.assertTrue(self.game.check_death(self.snake_inside))
        self.assertTrue(self.game.check_death(self.snake_wall))


if __name__ == '__main__':
    unittest.main()