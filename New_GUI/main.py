from flask import *

app = Flask(__name__)

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

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

if __name__ == "__main__":
    app.run(debug=True)