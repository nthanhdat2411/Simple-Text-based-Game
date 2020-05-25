from player import Player

class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.name = name
        self.hotkey = hotkey
        self.kwargs = kwargs
        #The kwargs variable is to make the Action class more flexible (it's possible to add in additional variables into the class).
        #Since different action will require different set of parameters. For example, attacking is different from moving to the next stage.

    def __str__(self):
        return '{}: {}'.format(self.hotkey, self.name)

class Move(Action):
    def __init__(self):
        super().__init__(method = Player.go_next_stage, name = 'Move to next stage', hotkey = 'g')

class ViewInfo(Action):
    def __init__(self):
        super().__init__(method = Player.print_info, name = 'View or edit player information', hotkey = 'v')

class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method = Player.attack, name = 'Attack', hotkey = 'a', enemy = enemy)
        #Althouugh the variable enemy here was not part of the Action class, it was bundled up into the kwargs variable.

class Fortification(Action):
    def __init__(self):
        super().__init__(method = Player.heal, name = 'Fortification', hotkey = 'f')

class Overdrive(Action):
    def __init__(self):
        super().__init__(method = Player.rage, name = 'Overdrive', hotkey = 'o')
