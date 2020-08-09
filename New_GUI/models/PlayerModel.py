class PlayerModel:
    def __init__(self, name):
        self.name = name
        self.kills = 0
        self.deaths = 0
        self.powerups = list()
        self._robotId = 0
        _generatePlayerId()

    def __init__(self, name: str, **kwargs):
        '''Build the model using kwargs.
        Values default to none.
        :param **kwargs: The list of class values that are set. (e.g.: deaths=5 sets deaths to 5).
        List of used kwargs: kills, deaths, powerups, robotId, playerId'''
        self.name = name
        self.kills = kwargs.pop('kills')
        self.deaths = kwargs.pop('deaths')
        self.powerups = kwargs.pop('powerups')
        self._robotId = kwargs.pop('robotId')
        self._playerId = kwargs.pop('playerId')

    def _generatePlayerId(self):
        self._playerId = 0

    def shoot(self, player):
        """This player shoots the player passed as an input.

        Returns: This players number of kills including this
        one
        :param player: The player who was shoot by this one"""
        self.kills += 1
        player.deaths += 1
        return self.kills
    
    def robotIsPlayer(self, robotId):
        '''Returns true if this player has a matching robot
        Id
        :param robotId: The robot id to check'''
        return self._robotId == robotId

    def generatePlayerHtml(self):
        return '''<td>
                    <h2>{self.name}</h2>
                    <b>Kills: </b>{self.kills}
                    <b>Deaths: </b>{self.deaths}
                    <h3>Power Ups:</h3>
                        {self.listPowerups()}
                </td>'''
    
    def listPowerups(self):
        out = ""

        for ii in self.powerups:
            out = out + '<p>{ii.name}</p>'
        
        return out

