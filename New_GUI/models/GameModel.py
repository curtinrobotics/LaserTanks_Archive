import time
import random
from models.PlayerModel import PlayerModel
from models.game.GameTypes import GameType
import json
from util.JsonUtil import convert_to_dict, dict_to_obj


class GameModel:
    
    def __init__(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, type'''
        self.__build(**kwargs)
        self.sortPlayers()

    def __build(self, **kwargs):
        '''Construct from any number of variables.
        :param **kwargs: Valid kwargs: gameId, startTime, players, type'''

        self.__gameId : int = kwargs.get('gameId', self.__generateId(kwargs.get("gameService")))
        self.startTime : float = kwargs.get('startTime', time.time())
        self.players : list[PlayerModel] = kwargs.get('players', list())
        self.type : str = kwargs.get('type', 'FFA')
        self.numPlayers = len(self.players)

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

        for ii in range(len(self.players)):
            self.players[ii].rank = ii + 1

    def getPlayerDictionary(self):
        players = list()

        for player in self.players:
            players.append({
                'name': player.name,
                'score': player.score, 
                'kills': player.kills,
                'deaths': player.deaths,
                'lives': player.lives,
                'rank': player.rank
                })
        
        return players
    
    def getPlaceSuffix(self, place):
            suffix = ''

            if place == 1: suffix = 'st'
            elif place == 2: suffix = 'nd'
            elif place == 3: suffix = 'rd'
            else: suffix = 'st'

            return suffix
    
    def getPlayer(self, id: int) -> PlayerModel:
        for p in self.players:
            if p.robotIsPlayer(id):
                return p
        
        return None

    def updatePlayers(self, *args : PlayerModel):
        '''Set each player in this GameModel to those
         contained in *args,
        Then update all players' ranks'''

        #set players to those in args
        if args != None:
            for player in args:
                if player != None:
                    for ii in range(len(self.players)):
                        if self.players[ii].robotIsPlayer(player.getId()):
                            player.updateScore()
                            self.players[ii] = player
                            break
        
        self.sortPlayers()

        #update rank
        for ii in range(self.numPlayers):
            score = self.players[ii].score
            rank = 4

            if score > 0:
                if ii > 0 and ii < 3:
                    #check if this player is tied with the previous
                    if score == self.players[ii-1].score:
                        rank = ii
                    else:
                        rank = ii + 1
                else:
                    rank = 1
            
            self.players[ii].rank = rank
            


    
    def serializePlayers(self):
        '''returns a json formatted string containing an array of players in this game'''
        return json.dumps(self.players, default=convert_to_dict, indent=2, sort_keys=True)
    
    def deserializePlayers(self, jsonString):
        '''deserialises players from a json string, 
        updates this games players and then returns the new players'''

        players = json.loads(jsonString, object_hook=dict_to_obj)
        self.updatePlayers(*players)

        return self.players

    def generateLeaderboardHtml(self):
        #returns a html formatted string for the leaderboard view
        
        html = '''
        <table class="game" ><tr><td></td>'''
            
        for player in self.players:
            html = html + '''<td align="center" id="{0}"><p class="header">{1}</p></td>'''.format(player.getId(), player.name)
            
        html = html + '''</tr><tr><td><b>Score</b></td>'''

        for player in self.players:
            html = html + '''<td align="center" id="{0}-score">{1}</td>'''.format(player.getId(), player.score)

        html = html + '''</tr><tr><td><b>Kills</b></td>'''

        for player in self.players:
            html = html + '''<td align="center" id="{0}-kills">{1}</td>'''.format(player.getId(), player.kills)
        
        html = html + '''</tr><tr><td><b>Deaths</b></td>'''
            
        for player in self.players:
            html = html + '''<td align="center" id="{0}-deaths">{1}</td>'''.format(player.getId(), player.deaths)
        
        html = html + '''</tr></table>'''

        return html
        
    def generateLeaderboardHtml(self):
        #returns a html formatted string for the leaderboard view

        html = ""
            
        for player in self.players:
            position = self.getPlayerDivPosition(player)

            html = html + '''<div class="board" id="player{0}" style="position: absolute;left: {5}%;top:45px;"><p class="header" id="player{0}">{1}</p><p class="score" id="player{0}">{2}</p><p class="kills" id="player{0}">{3}</p><p class="deaths" id="player{0}">{4}</p></div>'''.format(
                player.rank, player.name, player.score, player.kills, player.deaths,
                position) #last arg is the position in %)


        return html
    
    def getPlayerDivPosition(self, player):
        position = 0
        rank = player.rank

        if player.rank > self.numPlayers:
            rank = self.players.index(player) + 1

        position = 100 * (rank / (self.numPlayers + 1))

        return position
