class Player(object):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid
        self.role = None
        self.party = None
        self.is_dead = False
        self.inspected_players = {} 
        self.tokens_posesion = 0
        self.poseido = False
