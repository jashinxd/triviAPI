from flask import Flask, render_template, request
import urllib2, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

#@app.route("/quiz/<movie>")

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
