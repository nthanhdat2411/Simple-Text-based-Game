import world
from player import Player

def play():
    world.load_map()
    player = Player()
    position = world.stage_exists(player.x, player.y)
    print(position)
    while player.is_alive() and not player.victory:
        position = world.stage_exists(player.x, player.y)
        position.player_update(player)
        #Check whether the player has anything to do in the current position
        if player.is_alive() and not player.victory:
            print('\nChoose an action:\n')
            available_actions = position.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
    if not player.is_alive():
        print('You have been defeated.')

if __name__ == '__main__':
    play()

