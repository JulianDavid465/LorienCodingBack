from pony.orm import *

db = Database()


class Game(db.Entity):
    name = Required(str)  # Preguntar si es UNIQUE o no


db.bind(provider="sqlite", filename="db.sqlite", create_db=True)
db.generate_mapping(create_tables=True)
