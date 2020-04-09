from flask import *
from FFA_form import *
import socket

app = Flask(__name__)
app.secret_key = 'development key'


@app.route("/", methods=['GET', 'POST'])
def index():
   print(request.method)
   if request.method == 'POST':
      if request.form.get('Free_For_All') == 'Free For All':
         print("Free_For_All")
         return redirect(url_for('FFA'))
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
         return render_template('ffa.html', form = form)
      else:
         print(form.language.data)
         print(form.data)#["language"])
         return "hello"
   else:
      return render_template("ffa.html", form = form)
def get_ip():
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
   IP = get_ip()
   app.run(debug=True, host=IP,port=5005)