from flask import *
from forms import *

app = Flask(__name__)
app.secret_key = 'development key'

@app.route("/",methods = ['POST', 'GET'])
def home():
   print("hello")
   if request.method == 'POST':
      if request.form.get('submit') == 'submit':
         user = request.form['nm']
         return redirect(url_for('success',name = user))
   else:
      return render_template("home.html",val = "50")

   return render_template("home.html",val = "50")

if __name__ == "__main__":
   app.run(debug=True)#host = '0.0.0.0',port=5005)