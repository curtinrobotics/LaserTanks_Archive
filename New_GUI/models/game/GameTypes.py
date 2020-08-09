from models import GameModel, PlayerModel
from enum import Enum, auto
import time

class WinClause(Enum):
        TIME = auto()
        STOCK = auto()
        MAXKILLS = auto()

class GameType:
    def __init__(self, **kwargs):
        self.stock: int = kwargs.get("stock", 0)
        self.timeLimit: float = kwargs.get("timeLimit", 0)
        self.maxKills: int = None
        self.clause: WinClause = kwargs.get("clause")
        
        if self.clause == None:
            self.get()

    def gameOver(self, game: GameModel):
        self.check

    def get(self):
            '''Returns the win clause enum based off the 
            FIRST non-None value in kwargs'''

            winClause : WinClause = None #the return var

            #get the first none null item
            if self.timeLimit != None:
                winClause = WinClause.TIME
            elif self.stock != None:
                winClause = WinClause.STOCK
            elif self.maxKills != None:
                winClause = WinClause.MAXKILLS
        
            return winClause

    def check(self, game: GameModel):
        clause = self
        win = WinClause()

        if clause == win.STOCK:
            return self.__checkStockClause(game.players)
        elif clause == win.TIME:
            return self.__checkTimeClause(game)
        elif clause == win.MAXKILLS:
            return self.__checkMaxKillsClause(game)
        else:
            return self.__checkAllClauses(game)
    
    def __checkStockClause(self, players):
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
    
    def __checkTimeClause(self, game: GameModel):
        gameOver = False
        timeLimit = game.type.timeLimit

        if time.time() - game.startTime > timeLimit:
            gameOver = True

        return gameOver

    def __checkMaxKillsClause(self, game: GameModel):
        maxKills = game.type.maxKills

        for p in game.players:
            if p.kills > maxKills:
                return True

        return False

    def __checkAllClauses(self, game: GameModel):
        clauses = list()

        #Append all clause outcomes to the clauses list
        clauses.append(self.__checkStockClause(game))
        clauses.append(self.__checkMaxKillsClause(game))
        clauses.append(self.__checkTimeClause(game))

        # if at least one of them is true, return true
        for clause in clauses:
            if clause:
                return True

        # else
        return False

class FFA(GameType):
    def __init__(self, timeLimit: float, stock: int = 3, **kwargs):
        #add params to kwargs
        kwargs["stock"] = stock 
        kwargs["timeLimit"] = timeLimit

        #set the win clause
        super.clause = WinClause.TIME

        super().__init__(**kwargs)
    

class Elimination(GameType):
    def __init__(self, stock: int, **kwargs):
        #add params to kwargs
        kwargs["stock"] = stock 

        #set the win clause
        super.clause = WinClause.STOCK

        super().__init__(**kwargs)

class TeamBattle(GameType):
    def __init__(self, maxKills: int, **kwargs):
        #add params to kwargs
        kwargs["maxKills"] = maxKills

        #set the win clause
        super.clause = WinClause.MAXKILLS

        super().__init__(**kwargs)