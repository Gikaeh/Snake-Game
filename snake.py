class Snake:
    def __init__(self, MAP_HEIGHT, body=None):
        if body:
            self.body = body
        else:
            self.body = [(5, MAP_HEIGHT // 2), (4, MAP_HEIGHT // 2), (3, MAP_HEIGHT // 2)]
        self.directions = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
        self.direction = self.directions['right']

    def update_snake(self, eaten):
        new_head = self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1]
        self.body.insert(0, new_head)

        if not eaten:
            self.body.pop(-1)

        eaten = False
        return eaten
