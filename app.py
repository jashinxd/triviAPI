from flask import Flask, render_template, request
import urllib2, json, appextended

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/quiz", methods=["GET", "POST"])
@app.route("/quiz/<tag>", methods=["GET", "POST"])
def quiz(tag="toprated"):
    if tag == "toprated":
        return appextended.topRated()
    else:
        return appextended.specMovie(tag)
   


@app.route("/results", methods=["GET","POST"])
def submission():
    button = request.form['button']
    print button
    if request.method == "GET":
        status = "giveup"
        return render_template("results.html", status = status)
    else:
        status = "submitted"
        return render_template("results.html", status = status)



if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
