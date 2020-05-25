import world
import random

class Player():
    def __init__(self):
        self.vitality = 40
        self.atk = 10
        self.hp = 5* self.vitality
        self.damage = 2* self.atk
        self.x, self.y = world.starting_position
        self.victory = False

    def print_info(self):
        print('============================')
        print('Vitality (VIT): ', self.vitality)
        print('Attack (ATK): ', self.atk)
        print('HP: ',self.hp)
        print('Damage: ',self.damage)
        print('Fortification Skill: Heals yourself by 200% of your current Damage.')
        print('Overdrive Skill: Pay 30 HP to increase your current Damage by 100% permanently')
        print('============================')
        
    def is_alive(self):
        return self.hp > 0

    def go_next_stage(self):
        self.x += 0
        self.y += 1 #move to the next stage
        print(world.stage_exists(self.x, self.y))

    def attack(self, enemy):
        enemy.hp -= self.damage
        if not enemy.is_alive():
            print('You have killed the {}!'.format(enemy.name))
        else:
            print('You have dealt {} damage to the {}. It still has {} HP remaining.'.format(self.damage, enemy.name, enemy.hp))

    def heal(self):
        self.hp += 2* self.damage
        if self.hp > 5*self.vitality:
            self.hp = 5*self.vitality
        print('============================')
        print('Fortification has been used.')
        print('Current HP: {}'.format(self.hp))
        print('Current Damage: {}'.format(self.damage))
        print('============================')

    def rage(self):
        self.hp -= 30
        self.damage *= 2
        if self.hp < 0:
            self.hp = 0
        print('============================')
        print('Overdrive has been used')
        print('Current HP: {}'.format(self.hp))
        print('Current Damage: {}'.format(self.damage))
        print('============================')

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            #if getattr was successful, execute the found method
            #kwargs was included in case that method needs additional objects (like attack method)
            action_method(**kwargs)
            
