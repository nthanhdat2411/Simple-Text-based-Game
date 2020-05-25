import enemies, actions, world
class MapStage:
    def __init__(self, x, y):
        self.x = x #longitude of the MapStage
        self.y = y #latitude of the MapStage
    def intro_text(self):
        raise NotImplementedError() #this is to check whether a MapStage was created correctly
    def player_update(self, player):
        raise NotImplementedError() #same as above
    def go_next_stage(self):
        moves = []
        if world.stage_exists(self.x, self.y):
            moves.append(actions.Move())
        return moves
    def available_actions(self):
        moves = self.go_next_stage()
        moves.append(actions.ViewInfo())
        return moves
        

class Start(MapStage):
    def __str__(self):
        return """
======================================================================
You wake up from a crashed plane.
You find out there are some unsual marks on your body which look like those from the zombies out there.
It seems that you were injected with some unknown liquid.
You are infected.
However, it seems that you are partially immune to it.
Thanks to which, you possess both human intelligence and the zombie-like power.
You forget about everything that happened and want to find survivors in this world.
However, it is of crucial importance to find a safe zone at the moment.
The zombies can smell of alive human and are coming closer.
======================================================================
(Instruction)
To perform an action, press the corresponded hotkey and then press ENTER.
You have some special abilities that you can perform while fighting the zombies. You can see the details about these abilities whenever you attempt to view or edit your information.
The game is divided into stages in which you will fight the zombies and improve your stats.
The combat system in this game is turn-based. During your turn, you can perform a certain action. After that, it is the enemy's turn to attack you if it's still alive.
At the start of a combat stage, the enemy has the priority to attack you first.
IMPORTANT: You are only alllowed to perform one action per turn. Hence, if you decided to use one of your special abilities, you would not be able to attack your enemy that turn.
Upon defeating a zombie, you are rewarded some bonus points.
After each combat stage, there will be a rest stage for you to spend your bonus points.
These bonus points can be spent on either your Vitality stat or Attack stat, improving your strength in combat.
IMPORTANT: You are not allowed to re-spec your added bonus points. Hence, use them carefully!
Good luck and have fun!
======================================================================
"""
    def player_update(self, player):
        pass

class AddReward(MapStage):
    def __init__(self, x, y, bonus_point):
        self.bonus_point = bonus_point
        super().__init__(x, y)
    def __str__(self):
        return 'Great! You have earned some bonus points. You can spend them on your ATK and VIT stats to improve your strength in combat.'
    def add_point(self, player):
        #This part is to ask the player which stats they want to spend their bonus points on
        while self.bonus_point > 0 :
            x = input('You have {} points remaining. Which stat do you want to spend a bonus point on [VIT/ATK]?'.format(self.bonus_point))
            if x == 'VIT':
                player.vitality += 1
                print('You have successfully added 1 point to your vitality.')
            elif x == 'ATK':
                player.atk += 1
                print('You have successfully added 1 point to your attack.')
            self.bonus_point -= 1
        if self.bonus_point == 0:
            print('You have 0 points remaining.')
    def player_update(self, player):
        self.add_point(player) #update the player's stats
        player.damage = 2* player.atk
        player.hp = 5* player.vitality
        #the player's hp and damage are reset after each battle

class EnemyStage(MapStage):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
    def player_update(self, player):
        if self.enemy.is_alive(): #if the zombie is alive, it's their turn to attack the player
            player.hp = player.hp - self.enemy.damage
            if player.hp < 0:
                player.hp = 0
            print('Enemy does {} damage. You have {} HP remaining.'.format(self.enemy.damage, player.hp))
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Attack(enemy = self.enemy), actions.Fortification(), actions.Overdrive()]
        else:
            return self.go_next_stage()

class Walker(EnemyStage):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Walker())
    def __str__(self):
        return """
============================
Enemy's HP: 100
Enemy's Damage: 20
The Walker is among the most popular types of zombies.
============================"""

class Stalker(EnemyStage):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Stalker())
    def __str__(self):
        return """
============================
Enemy's HP: 500
Enemy's Damage: 60
The Stalker enjoys jumping and attacking from behind.
Although it seems deadly, it has low stamina.
============================"""

class Charger(EnemyStage):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Charger())
    def __str__(self):
        return """
============================
Enemy's HP: 2500
Enemy's Damage: 55
This thing, called the Charger, is one of the worst nightmares for any living thing.
It's fast and endurance.
============================"""

class Wrestler(EnemyStage):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Wrestler())
    def __str__(self):
        return """
============================
Enemy's HP: 3000
Enemy's Damage: 80
It's big. It's strong. It can throw even a huge truck.
It's called the Wrestler.
============================"""

class Smoker(EnemyStage):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Smoker())
    def __str__(self):
        return """
============================
Enemy's HP: 4000
Enemy's Damage: 85
Legends said that any creature trying to get close to the Smoker has stopped breathing.
============================"""
        
class Berserker(EnemyStage):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Berserker())
    def __str__(self):
        return """
============================
Enemy's HP: 500
Enemy's Damage: 100
You must be very unlucky to be facing the Berserker.
One of the deadliest zombies ever existed.
============================"""

class Warrior(EnemyStage):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Warrior())
    def __str__(self):
        return """
============================
Enemy's HP: 1000000
Enemy's Damage: 100
An unknown Warrior. Jumping out from a cave.
============================"""

class EndOfMap(MapStage):
    def __str__(self):
        return """
=======================================================
The Warrior: "You will pay for what you've done..."
This thing can talk! How is that possible?
And what does he mean by that?
Is he one with the same identity as yours? Half human, half zombie?
Why did he attack you?
Although he can talk, his appearance is not like human at all.
He looks just about the same as those zombies out there.
What happened in this world while you blackened out?
Is there a hidden story behind this zombie apocalypse?
Is there really a cure for this disease?
There are so many questions in your head.
But for now, you need to save yourself from the unending zombie hordes out there.
The Warrior's cave is quite a nice place for you to stay in.
As you walk into the cave, you find an old cassette player.
You turn it on.
A male voice starts speaking. "April 20, 2069. We are on a plane to Los Angeles. So there's this rescue mission..."
========================================================
THE END.
"""
    def player_update(self, player):
        player.victory = True


