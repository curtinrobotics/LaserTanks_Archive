from models.game import Powerup
from random import randint
from app import db

class PlayerModel:
    self.name : str = name
    self.kills : int = kwargs.get('kills', 0)
    self.lives : int = kwargs.get('lives', 0)
    self.deaths : int = kwargs.get('deaths', 0)
    self.score = 0
    self.powerups : list[Powerup] = kwargs.get('powerups', list())
    self.timeDied : float = None
    self.__robotId : int = kwargs.get('robotId', self.__generateId())
    self.__playerId : int = kwargs.get('playerId', self.__generateId())

    def __init__(self, name: str, **kwargs):
        '''Build the model using kwargs.
        Values default to none.
        :param **kwargs: The list of class values that are set. (e.g.: deaths=5 sets deaths to 5).
        List of used kwargs: kills, deaths, powerups, robotId, playerId'''

        self.__build(name=name, **kwargs)

    def __build(self, name:str, **kwargs):
        '''Build the model using kwargs.
        Values default to none.
        :param name: The player's name
        :param **kwargs: The list of class values that are set. (e.g.: deaths=5 sets deaths to 5).
        List of used kwargs: kills, deaths, powerups, robotId, playerId'''

        self.name : str = name
        self.kills : int = kwargs.get('kills', 0)
        self.lives : int = kwargs.get('lives', 0)
        self.deaths : int = kwargs.get('deaths', 0)
        self.score = 0
        self.powerups : list[Powerup] = kwargs.get('powerups', list())
        self.timeDied : float = None
        self.__robotId : int = kwargs.get('robotId', self.__generateId())
        self.__playerId : int = kwargs.get('playerId', self.__generateId())

    def __generateId(self):
        return randint(1000, 9999)

    def shoot(self, player):
        """This player shoots the player passed as an input.

        Returns: This players number of kills including this
        one
        :param player: The player who was shoot by this one"""
        self.kills += 1
        player.deaths += 1

        #update scores
        self.updateScore()
        player.updateScore()

        return self.kills
    
    def robotIsPlayer(self, robotId):
        '''Returns true if this player has a matching robot
        Id
        :param robotId: The robot id to check'''
        return self._robotId == robotId
    
    def kill(self):
        '''Increment this player's kills and return the number'''
        self.kills += 1
        return self.kills

    def die(self):
        '''Increment this player's deaths and return the number'''
        self.deaths += 1
        return self.deaths


    def getId(self):
        return self.__robotId
    
    def updateScore(self):
        kills = self.kills
        deaths = self.deaths
        score = 2 * (kills + 1) - deaths
        self.score = score
    
    def listPowerups(self):
        out = ""

        for ii in self.powerups:
            out = out + '<p>{ii.name}</p>'
        
        return out


