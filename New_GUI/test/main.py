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

@app.route("/about", methods = ['GET', 'POST'])
def about():
   return render_template("about.html")

@app.route('/success/<name>')
def success(name):
   """
   success [summary]
   
   Parameters
   ----------
   name : [type]
       [description]
   
   Returns
   -------
   [type]
       [description]
   """
   print("hello")
   if request.method == 'POST':
      print("ght")
      if request.form.get('submit1') == 'submit1':
         return 'welcome'
   else:
      return render_template("test.html",n = '50')

   #return render_template("test.html")
   #return 'welcome %s' % name
   #return render_template("test.html")

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         print(form.language.data)
         print(form.data)#["language"])
         return render_template('about.html')
   else:
      return render_template('contact.html', form = form)

if __name__ == "__main__":
   app.run(debug=True)#host = '0.0.0.0',port=5005)

