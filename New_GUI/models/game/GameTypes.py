from models.GameModel import GameModel
from models.PlayerModel import PlayerModel
from enum import Enum, auto
import time

class WinClause(Enum):
        TIME = auto()
        STOCK = auto()
        MAXKILLS = auto()

        def get(self, **kwargs):
            '''Returns the win clause enum based off the 
            FIRST non-None value in kwargs'''

            winClause = WinClause() #the return var

            for key, value in kwargs.items():
                #get the first none null item
                if value != None:
                    if key == "time":
                        winClause = self.TIME
                    elif key == "stock":
                        winClause = self.STOCK
                    elif key == "maxKills":
                        winClause = self.MAXKILLS
                    #then exit the loop
                    break
            
            return winClause

        def check(self, game: GameModel):
            clause = self
            win = WinClause()

            if clause == win.STOCK:
                return self.__checkStockClause(game.players)
            elif clause == win.TIME:
                return self.__checkTimeClause(game.timeElapsed, game.rules)
            elif clause == win.MAXKILLS:
        
        def __checkStockClause(players: list(PlayerModel)):
            numPlayers = len(players)
            deadPlayers = 0
            gameOver = False

            #for each dead player, increment dead players
            for p in players:
                if p.lives == 0:
                    deadPlayers += 1

            #if there's at most one player alive, the game is over
            if deadPlayers >= numPlayers - 1:
                gameOver = True

            return gameOver

class IGameType:
    def gameOver(self, game: GameModel):
        raise NotImplementedError

class FFA(IGameType):
    def __init__(self, timeLimit: time = None, stock: int = 3, maxKills = None):
        self.stock = stock
        self.time = timeLimit
        self.maxKills = None
        self.clause : WinClause = WinClause.get(stock=stock, time=timeLimit, maxKills=maxKills)

    def gameOver(self, game: GameModel):
        return self.clause.check()
    

class Elimination(IGameType):
class TeamBattle(IGameType):