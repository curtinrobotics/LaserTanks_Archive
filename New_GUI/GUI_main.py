from flask import *
from FFA_form import *
import socket
import os
from Function import player

app = Flask(__name__)
app.secret_key = 'development key'


@app.route("/", methods=['GET', 'POST'])
def index():
   print(request.method)
   if request.method == 'POST':
      if request.form.get('Free_For_All') == 'Free For All':
         print("Free_For_All")
         try:
            return redirect(url_for('FFA'))
         except:
            return "page not found"
      elif  request.form.get('Team') == 'Team':
         print("Team")
      else:
         return render_template("home.html")
   elif request.method == 'GET':
      print("No Post Back Call")
   return render_template("home.html")

@app.route("/Free_For_All", methods = ['GET', 'POST'])
def FFA():
   form = FFAF()
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         print(form.Nom_player.data)
         player_nom = form.Nom_player.data
         column = player(player_nom)
         print(column)
         return render_template('ffa.html', form = form,column=column)
      else:
         print(form.Nom_player.data)
         return "hello"
   else:
      try:
         return render_template("ffa.html", form = form)
      except:
         return "page not found"


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
   url_for('static', filename="plugin/highlight/monokai.css")
   url_for('static', filename="dist/reveal.js")
   url_for('static', filename="plugin/highlight/highlight.js")
   url_for('static', filename="LaserTank.png")

   app.run(debug=True, host=IP,port=5005)