from flask import *
from FFA_form import *
import socket
import os
from Function import player
from services.TemplateService import generateTemplate

app = Flask(__name__, static_folder="static")
app.secret_key = 'development key'


@app.route("/")
def index():
   return render_template("home.html")

@app.route("/New-Game", methods = ['GET'])
def newGame():
   return render_template("new-game.html")

@app.route("/Setup", methods = ['GET', 'POST'])
def setup():
   gameType = request.form["Type"]
   numPlayers = int(request.form["Players"])
   templateInjection = generateTemplate(numPlayers)

   return render_template("setup-players.html", injection=templateInjection, type=gameType)

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