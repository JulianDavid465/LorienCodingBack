from pony.orm import Database, Required, Optional, Set
from pony.orm import db_session, select, count

games = Database()

class Game(games.Entity):  
    name = Required(str)         # Preguntar si es UNIQUE o no
    gameStatus = Required(int)                  # 0 = Open, 1 = InGame                

# Configuramos la base de datos. 
# Más info: https://docs.ponyorm.org/database.html
games.bind('sqlite', 'game.sqlite', create_db=True)  # Conectamos el objeto `db` con la base de dato.
games.generate_mapping(create_tables=True)  # Generamos las base de datos.

""""
## The db_session() decorator performs the following actions on exiting function:
#
#  - Performs rollback of transaction if the function raises an exception
#  - Commits transaction if data was changed and no exceptions occurred
#  - Returns the database connection to the connection pool
#  - Clears the database session cache

@db_session
def addGame(name : str):
    Game(name = name, gameStatus = 0)

@db_session
def getGames():
    return select(game.name for game in Game)[:]
"""


@db_session
def addData():
    Game(name = "1ra partida", gameStatus = 0)
    return select(game.name for game in Game)[:]