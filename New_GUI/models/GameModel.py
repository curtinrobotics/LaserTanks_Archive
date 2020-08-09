import time

class GameModel:
    def __init__(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, rules'''
        self.build(kwargs)

    def build(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, rules'''

        self._gameId = kwargs.pop('gameId')
        self.startTime = kwargs.pop('startTime')
        self.players = kwargs.pop('players')
        self.rules = kwargs.pop('rules')

        if self._gameId == None:
            raise NameError
    
    def timeElapsed(self):
        currentTime = time.time()
        return currentTime - self.startTime
