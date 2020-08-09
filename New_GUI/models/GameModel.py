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

    def generateLeaderboard(self):
        '''Returns a string containing html text of the players rendered in order'''
        playerHtmls = list() #return var

        def sortFunc(player: PlayerModel):
            return player.score()

        def getPlaceSuffix(place):
            suffix = ''

            if place == 1: suffix = 'st'
            elif place == 2: suffix = 'nd'
            elif place == 3: suffix = 'rd'
            else: suffix = 'st'

            return suffix

        self.players.sort(reverse=True, key=sortFunc)
        count = 0 #temp var

        for p in self.players:
            html = p.generatePlayerHtml()

            html = "<h2>{0}{1} Place</h2><br>".format(count + 1, getPlaceSuffix(count+1)) + html

            if count % 2 == 0:
                html = "<tr>" + html
            elif count % 2 == 1:
                html = html + "</tr>"

            count += 1
        
        html = '<table>' + html + '</table>'

        return html
