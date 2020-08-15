from flask import *
from flask_socketio import SocketIO, emit
import socket
import os
import time
from util.HttpUtil import validateRequest

from models import GameModel, PlayerModel

app = Flask(__name__, static_folder="static")
app.secret_key = 'development key'

currentGame = GameModel.GameModel()

style=""

if True:
   styleFile = open("static/styles/main.css", "r")
   style = styleFile.read()
   styleFile.close()

def setGame(**kwargs):
   currentGame = GameModel.GameModel(startTime=time.time(), **kwargs)
   currentGame.sortPlayers()

@app.route("/")
def index():
   return render_template("HomeView.html", style=style)

@app.route("/New-Game", methods = ['GET'])
def newGame():
   """Asks for game type and number of players
   so that further details can be obtained in validation"""
   return render_template("NewGameView.html", style=style)

@app.route("/Setup", methods = ['GET', 'POST'])
def setup():
   #redirect to new game page if this page was accessed with a URL
   if request.method == 'GET':
      return redirect("/New-Game")

   try:
      validateRequest(request, "Type", "Players")
   except KeyError:
      return redirect("/New-Game")

   
   gameType = request.form["Type"]
   numPlayers = int(request.form["Players"])

   return render_template("NewGameSetupView.html", numPlayers=numPlayers, style=style, type=gameType)

@app.route("/Game", methods = [ 'POST'])
def createGame():
   #get game type
   gameType = request.form["type"]
   numPlayers = int(request.form["numPlayers"])

   #create players
   players = list()

   for ii in range(1, numPlayers + 1):
      name = str(request.form["player%d" % ii])
      players.append(PlayerModel.PlayerModel(name))

   #create gameModel
   currentGame = GameModel.GameModel(time=time.time(), players=players, type=gameType)

   return render_template("GameView.html", game=currentGame, style=style)

@app.route("/Test", methods = ['GET'])
def testEndpoint():
   return "Success!"

'''Flask Endpoints'''
'''Shoot Enpoint'''
@app.route('/Game/Shoot/<robotId>', methods=['GET'])
def shoot(robotId):
   shootee = currentGame.getPlayer(int(robotId))
   shooter = currentGame.getPlayer(int(request.headers['shooter']))

   if shooter != None and shootee != None:
      #increment respective players' kills and deaths
      #  then update them for the current game and send
      #  a socket event

      kills = shooter.kill()
      deaths = shootee.die()
      currentGame.updatePlayers(shooter, shootee)

      emit('shoot', {'shooter': shooterId, 'shootee': robotId, 'kills': kills, 'deaths': deaths})


def get_ip():
   """
   get_ip: Get the IP address from the host
   
   Returns
   -------
   IP
       The IP address of the host
   """
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   try:
      # doesn't even have to be reachable
      s.connect(('10.255.255.255', 1))
      IP = s.getsockname()[0]
   except:
      IP = '127.0.0.1'
   finally:
      s.close()
   return IP
   
if __name__ == '__main__':
   """
    main function
   """
   IP = get_ip()
   
   url_for('static', filename="dist/reveal.css")
   url_for('static', filename="dist/theme/black.css")
   url_for('static', filename="dist/theme/style_overlay.css")
   url_for('static', filename="plugin/highlight/monokai.css")
   url_for('static', filename="dist/reveal.js")
   url_for('static', filename="plugin/highlight/highlight.js")
   url_for('static', filename="LaserTank.png")

   
   app.run(debug=True, host=IP,port=5005)