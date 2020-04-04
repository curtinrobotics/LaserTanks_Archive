from flask import *


app = Flask(__name__)
app.secret_key = 'development key'


@app.route("/", methods=['GET', 'POST'])
def index():
   print(request.method)
   if request.method == 'POST':
      if request.form.get('Free_For_All') == 'Free For All':
            # pass
            print("Free_For_All")
      elif  request.form.get('Team') == 'Team':
            # pass # do something else
            print("Team")
      else:
            # pass # unknown
            return render_template("Home.html")
   elif request.method == 'GET':
      # return render_template("index.html")
      print("No Post Back Call")
   return render_template("Home.html")


if __name__ == '__main__':
   app.run(debug=True, host='10.1.1.148',port=5005)