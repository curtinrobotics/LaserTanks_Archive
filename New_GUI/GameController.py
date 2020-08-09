from flask import *
from FFA_form import *
import socket
import os
from Function import player
from services.TemplateService import generateTemplate

app = Flask(__name__, static_folder="static")
app.secret_key = 'development key'

style=""

if True:
   styleFile = open("static/styles/main.css", "r")
   style = styleFile.read()
   styleFile.close()



@app.route("/")
def index():
   return render_template("home.html", style=style)

@app.route("/New-Game", methods = ['GET'])
def newGame():
   """Asks for game type and number of players
   so that further details can be obtained in validation"""
   return render_template("new-game.html", style=style)

@app.route("/Setup", methods = ['GET', 'POST'])
def setup():
   if request.method == 'GET':
      return redirect("/New-Game")
   
   gameType = request.form["Type"]
   numPlayers = int(request.form["Players"])

   return render_template("setup-players.html", numPlayers=numPlayers, style=style, type=gameType)

@app.route("/Create-Game", methods = [ 'POST'])
def createGame():
   return render_template("Game-View.html")


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