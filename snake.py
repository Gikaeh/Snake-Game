class Snake:
    def __init__(self, MAP_HEIGHT, body=None):
        if body:
            self.body = body
        else:
            self.body = [(5, MAP_HEIGHT // 2), (4, MAP_HEIGHT // 2), (3, MAP_HEIGHT // 2)]
        self.directions = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
        self.direction = self.directions['right']
        self.bodyCount = 3

    def get_snake_body(self):
        return self.body
    
    def get_body_count(self):
        return self.bodyCount
    
    def set_snake_body(self, n):
        self.body = n

    def set_body_count(self, n):
        self.bodyCount = n

    def update_snake(self, game):
        new_head = self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]
        self.body.insert(0, new_head)

        if not game.get_eaten():
            self.body.pop(-1)

        if game.get_eaten():
            self.bodyCount += 1

        game.set_eaten(False)
        return self.bodyCount
