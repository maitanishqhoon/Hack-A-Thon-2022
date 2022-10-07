from flask import Flask, render_template, request
app = Flask(__name__)
result={'resp':True}

@app.route('/',methods = ['POST', 'GET'])
def result():
   return render_template("home.html")

if __name__ == '__main__':
   app.run(debug = True)