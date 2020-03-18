from flask import *

app = Flask(__name__)
app.secret_key = 'development key'

@app.route("/",methods = ['POST', 'GET'])
def home():
   print("hello")
   if request.method == 'POST':
      
      if request.form.get('Free_For_All') == 'Free For All':
         print('hello')
      else:
         print('hello34')
   else:
      return render_template("Home.html",val = "50")

   return render_template("Home.html",val = "50")

@app.route('/success')
def success():
   print("hello")
   if request.method == 'POST':
      print("ght")
      if request.form.get('submit1') == 'submit1':
         return 'welcome p' 
   else:
      return render_template("test.html",n = '50')

   #return render_template("test.html")
   #return 'welcome %s' % name
   #return render_template("test.html")


if __name__ == "__main__":
   app.run(debug=True, host='192.168.0.7',port=5005)