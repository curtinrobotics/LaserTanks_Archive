#!/usr/bin/env python
from threading import Lock
from flask import *
from flask import appcontext_pushed, g
from flask_socketio import SocketIO, emit
import socket
import os
import sys
import time
from util.HttpUtil import validateRequest


from models import GameModel, PlayerModel

app = Flask(__name__, static_folder="static")
app.secret_key = 'development key'

#global vars
currentGame : GameModel = None
style=""

#socket settings
thread = None
thread_lock = Lock()

# Set this variable to "threading", "eventlet" or "gevent" to test the
# different async modes, or leave it set to None for the application to choose
# the best option based on installed packages.
async_mode = None

socketio = SocketIO(app, async_mode=async_mode)

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        socketio.sleep(10)
        count += 1
        socketio.emit('my_response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


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
   ids = [8056, 6828, 9321, 2234]

   for ii in range(1, numPlayers + 1):
      name = str(request.form["player%d" % ii])
      players.append(PlayerModel.PlayerModel(name, robotId=ids[ii-1]))

   #create gameModel and make it global
   global currentGame
   currentGame = GameModel.GameModel(time=time.time(), players=players, type=gameType)

   return render_template("GameView.html", game=currentGame, style=style, async_mode=socketio.async_mode)

@app.route("/Test", methods = ['GET'])
def testEndpoint():
   return "Success!"

'''Flask Endpoints'''
'''Shoot Enpoint'''
@app.route('/Game/Shoot/<robotId>', methods=['GET'])
def shoot(robotId):
   global currentGame

   try:
      shootee = currentGame.getPlayer(int(robotId))
      shooter = currentGame.getPlayer(int(request.headers['shooter']))

      if shooter != None and shootee != None:
         #increment respective players' kills and deaths
         #  then update them for the current game and send
         #  a socket event

         kills = shooter.kill()
         deaths = shootee.die()
         currentGame.updatePlayers(shooter, shootee)

         renderLeaderboard()
         return jsonify({'shooter': shooter.getId(), 'shootee': shootee.getId(), 'kills': kills, 'deaths': deaths})
      else:
         return make_response(jsonify({'error': 'Players not found'}), 404)
   except NameError as err:
      return make_response(jsonify({'error': 'No current game instance running'}), 404)
   except Exception as err:
      return make_response(jsonify({'unexpected-error': sys.exc_info[0]}), 500)
   
@app.errorhandler(404)
def notFound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#Socket Stuff
@socketio.on('connect', namespace='/Game')
def connect():
   global thread
   with thread_lock:
      if thread is None:
         thread = socketio.start_background_task(background_thread)
   renderLeaderboard()

def renderLeaderboard():
   global currentGame
   currentGame.updatePlayers()

   emit('render', {'html': currentGame.generateLeaderboardHtml()}, namespace='/Game', broadcast=True)


def sendPlayerData():
   global currentGame
   if currentGame != None:
      dictionary = currentGame.getPlayerDictionary()
      emit('playerData', {'players': dictionary}, namespace='/Game', broadcast=True)

def sendGameData():
   global currentGame
   if currentGame != None:
      emit('gameData', json.dumps({
            'game': 
            { 
               'numPlayers': currentGame.numPlayers,
               'gameTime': currentGame.timeElapsed(),
               'players': currentGame.getPlayerDictionary()
            }
         }), namespace='/Game', broadcast=True)

@socketio.on('disconnect_request', namespace='/Game')
def disconnect_request():
    @copy_current_request_context
    def can_disconnect():
        disconnect()

@socketio.on('response', namespace='/Game')
def response(message):
   print(message.data)

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

   
   socketio.run(app, debug=True, host=IP,port=5005)