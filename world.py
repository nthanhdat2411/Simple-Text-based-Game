import stages

_world = {}
starting_position = (0, 0) #the first point in the room

def load_map():
    #Pass the file map.txt that describes the world into the _world object
    with open('map.txt', 'r') as f:
        rows = f.readlines()
    for y in range(len(rows)):
        stage_name = rows[y].replace('\n','')
        if stage_name == 'Start':
            global starting_position
            starting_position = (0, y)
            _world[(0,y)] = stages.Start(0,y)
        if stage_name == 'Walker' :
            _world[(0,y)] = stages.Walker(0,y)
        if stage_name == 'Stalker':
            _world[(0,y)] = stages.Stalker(0,y)
        if stage_name == 'Charger':
            _world[(0,y)] = stages.Charger(0,y)
        if stage_name == 'Berserker':
            _world[(0,y)] = stages.Berserker(0,y)
        if stage_name == 'AddReward':
            _world[(0,y)] = stages.AddReward(0,y,5)
        if stage_name == 'Wrestler':
            _world[(0,y)] = stages.Wrestler(0,y)
        if stage_name == 'Smoker':
            _world[(0,y)] = stages.Smoker(0,y)
        if stage_name == 'Warrior':
            _world[(0,y)] = stages.Warrior(0,y)
        if stage_name == 'EndOfMap':
            _world[(0,y)] = stages.EndOfMap(0,y)
        

def stage_exists(x, y):
    return _world[(x, y)]

load_map()

