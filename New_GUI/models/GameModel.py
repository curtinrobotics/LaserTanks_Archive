import time
import random
from models import PlayerModel
from models.game.GameTypes import GameType


class GameModel:
    def __init__(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, type'''
        self.__build(**kwargs)

    def __build(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, type'''

        self.__gameId : int = kwargs.get('gameId', self.__generateId(kwargs.get("gameService")))
        self.startTime : float = kwargs.get('startTime', time.time())
        self.players : list[PlayerModel] = kwargs.get('players', list())
        self.type : GameType = kwargs.get('type', GameType())

    def __generateId(self, gameService):
        if gameService == None:
            self.__gameId = random.randint(10000, 99999)
    
    def timeElapsed(self):
        currentTime = time.time()
        return currentTime - self.startTime

    def sortPlayers(self):
        def sortFunc(player: PlayerModel):
            return player.score

        self.players.sort(reverse=True, key=sortFunc)
    
    def getPlaceSuffix(place):
            suffix = ''

            if place == 1: suffix = 'st'
            elif place == 2: suffix = 'nd'
            elif place == 3: suffix = 'rd'
            else: suffix = 'st'

            return suffix