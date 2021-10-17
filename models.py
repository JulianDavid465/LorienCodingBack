from pony.orm import *

db = Database()


class Player(db.Entity):
    id = Required(int, unsigned=True)
    nickName = Required(str)
    gameID = Required("Game")
    isHost = Optional(bool, default=False)
    PrimaryKey(id, gameID)


class Game(db.Entity):
    id = PrimaryKey(int, auto=True, unsigned=True)
    name = Required(str)
    password = Optional(str)
    state = Required(int, default=0)
    playersID = Set(Player, cascade_delete=False)

    # 0 = 'Waiting Players'
    # 1 = 'Started'
    # -1 = 'Ended'


db.bind(provider="sqlite", filename="db.sqlite", create_db=True)
db.generate_mapping(create_tables=True)
