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
      return render_template("home.html")

   return render_template("home.html")

@app.route("/about", methods = ['GET', 'POST'])
def about():
   return render_template("about.html")

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
   form = ContactForm()
   
   if request.method == 'POST':
      if form.validate() == False:
         flash('All fields are required.')
         return render_template('contact.html', form = form)
      else:
         print(form.name)
         return render_template('about.html')
   else:
      return render_template('contact.html', form = form)


if __name__ == "__main__":
    app.run(debug=True)