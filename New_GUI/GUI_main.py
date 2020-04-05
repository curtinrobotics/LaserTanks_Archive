from flask import *
from FFA_form import *

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
         return render_template("Home.html")
   elif request.method == 'GET':
      print("No Post Back Call")
   return render_template("Home.html")

@app.route("/Free_For_All", methods = ['GET', 'POST'])
def FFA():
   form = FFAF()
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         print(form.language.data)
         print(form.data)#["language"])
         return "hello"
   else:
      return render_template("contact.html", form = form)

if __name__ == '__main__':
   app.run(debug=True, host='10.1.1.148',port=5005)