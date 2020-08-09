import time
from models import PlayerModel
from models.game import Rule
from models.game.GameTypes import IGameType


class GameModel:
    def __init__(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, type'''
        self.__build(kwargs)

    def __build(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, type'''

        self._gameId : int = kwargs.pop('gameId')
        self.startTime : float = kwargs.pop('startTime')
        self.players : list(PlayerModel) = list(kwargs.pop('players'))
        self.type : IGameType = kwargs.pop('type')

        if self._gameId == None:
            raise NameError
    
    def timeElapsed(self):
        currentTime = time.time()
        return currentTime - self.startTime
