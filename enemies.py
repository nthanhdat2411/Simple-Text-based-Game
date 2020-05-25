class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def is_alive(self):
        return self.hp > 0 #check for the boolean variable of whether the current hp is > 0 or not

class Walker(Enemy):
    def __init__(self):
        super().__init__(name = 'Walker', hp = 100, damage = 20)

class Stalker(Enemy):
    def __init__(self):
        super().__init__(name = 'Stalker', hp = 500, damage = 60)

class Charger(Enemy):
    def __init__(self):
        super().__init__(name = 'Charger', hp = 2500, damage = 55)

class Wrestler(Enemy):
    def __init__(self):
        super().__init__(name = 'Wrestler', hp = 3000, damage = 80)

class Smoker(Enemy):
    def __init__(self):
        super().__init__(name = 'Smoker', hp = 4000, damage = 85)

class Berserker(Enemy):
    def __init__(self):
        super().__init__(name = 'Berserker', hp = 500, damage = 100)

class Warrior(Enemy):
    def __init__(self):
        super().__init__(name = 'Warrior', hp = 1000000, damage = 100)
