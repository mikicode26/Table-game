from exceptions import GameOver
from exceptions import EnemyDown
from random import randint

class Player:

    def __init__(self, name, lives, score=0):
        self.name = name
        self.lives = lives
        self.score = score

    def select_attack(self):
        '''
        select attack, valid only 1,2,3
        :return: int(attack)
        '''
        attack = input("Выберите атаку (1 - камень, 2 - ножницы, 3 - бумага): ")
        while attack not in ['1', '2', '3']:
            attack = input('Неверный выбор. Выберите атаку (1 - камень, 2 - ножницы, 3 - бумага): ')
        return int(attack)

    def decrease_lives(self):
        '''
        decrease lives
        :return: None, only raise GameOver
        '''
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def add_score(self):
        # add score for Player
        self.score += 1
        if self.score == 1:
            return 2
        elif self.score == 5:
            return 10

class Enemy:

    def __init__(self, level, lives):
        self.level = level
        self.lives = lives

    def select_attack(self):
        return random.randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown