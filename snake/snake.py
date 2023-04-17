import pygame

class Snake:
    def __init__(self, x, y):
        self.head = (x, y)
        self.body = [(x, y)]

    def move(self, dx, dy):
        x, y = self.head
        self.head = (x + dx, y + dy)
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i-1]
        self.body[0] = self.head

    def grow(self):
       self.body.append(self.body[-1])

    def is_collision(self, x, y):
        (head_x, head_y) = self.head
        return head_x == x and head_y == y

    def is_self_collision(self):
        return self.head in self.body[1:]