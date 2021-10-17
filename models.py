from pony.orm import *

db = Database()


class Game(db.Entity):
    id = PrimaryKey(int, auto=True, unsigned=True)
    name = Required(str)


db.bind(provider="sqlite", filename="db.sqlite", create_db=True)
db.generate_mapping(create_tables=True)
