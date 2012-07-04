#!/usr/bin/env python
# game.py - simple game to demonstrate classes and objects

world = [[None] * 100] * 100

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        world[x][y] = self
    
    def remove(self):
        world[self.x][self.y] = None

class Character(Entity):
    def __init__(self, x, y, hp):
        Entity.__init__(self, x, y)
        self.hp = hp
        self.items = []
    
    def moveLeft(self):
        self.x -= 1
    
    def moveRight(self):
        self.x += 1

    def attack(self, enemy):
        if abs(enemy.x - self.x) == 1 and (enemy.y == self.y):
            enemy.hp -= 10

class Wizard(Character):
    def __init__(self, x, y, hp):
        Character.__init__(self, x, y, hp)
    
    def castSpell(self, enemy):
        if abs(enemy.x - self.x) == 1 and (enemy.y == self.y):
            enemy.remove()

class Archer(Character):
    def __init__(self, x, y, hp):
        Character.__init__(self, x, y, hp)
    
    def rangeAttack(self, enemy):
        if abs(enemy.x - self.x) <= 5 and (enemy.y == self.y):
            enemy.hp -= 5
