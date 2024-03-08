from models import Enemy
from exceptions import GameOver
from exceptions import EnemyDown

class Game:

    def __init__(self, player, mode):
        self.player = player
        self.mode = mode
        self.enemy = Enemy(level=1, difficulty=mode)

    def create_enemy(self):
        # create new enemy
        self.enemy = Enemy(level=self.enemy.level +1, difficulty=self.mode)

    def play(self):
        # play game
        while True:
            try:
                self.fight()
            except GameOver:
                print("Game Over! You lost all your lives")
                self.save_score()
                break
            except EnemyDown:
                print(f"You defeated level {self.enemy.level} enemy!")
                self.player.add.score()
                self.create_enemy()

    def fight(self):
        '''
        Ask attack player and enemy
        '''
        player_attack = self.player.select_attack()
        enemy_attack = self.enemy.select_attack()
        result = (player_attack - enemy_attack) % 3
        self.handle_fight_result(result)

    def handle_fight_result(self, result: int):
        '''
        Handle fighting
        :param result: win, draw, fail
        '''
        if result == 1:
            print("You win!")
            self.enemy.decrease_lives()
        elif result == 0:
            print("You draw!")
        else:
            print("You fail!")
            self.player.decrease_lives()

    def save_score(self):
        # return: save score and life
        score = self.player.score