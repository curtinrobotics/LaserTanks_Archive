import time
from flask import request
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

    def buildFromForm(self, inRequest: request):
        #get game type
        gameType = inRequest.form["type"]

        #create players
        players = list(PlayerModel)

        for ii in range(0, inRequest.form["numPlayers"] + 1):
            name = inRequest.form["player%d" % ii]
            players.append(PlayerModel.PlayerModel(name))

        #create gameModel
        game = self.__build(startTime=time.time(), players=players, type=gameType)
    
    def timeElapsed(self):
        currentTime = time.time()
        return currentTime - self.startTime

    def generateLeaderboard(self):
        '''Returns a string containing html text of the players rendered in order'''
        playerHtmls = list() #return var

        def sortFunc(p: PlayerModel):
            return p.score()

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
