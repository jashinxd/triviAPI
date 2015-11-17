from flask import Flask, render_template, request
import urllib2, json, appextended

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/quiz", methods=["GET", "POST"])
def quiz(tag="toprated"):
    if tag == "toprated":
        return appextended.topRated()
    else:
        return appextended.specMovie(tag)


@app.route("/quiz/<tag>", methods=["GET", "POST"])
def submission(tag):
    if request.method == "GET": 
        return appextended.specMovie(tag)
    else:
        key = "bb8c8b5dede831baad7b87391d01d20c"
        creds = "append_to_response=credits"
        uri = "https://api.themoviedb.org/3/movie/%s?api_key=%s&%s"
        url = uri%(tag, key, creds)
        
        requested = urllib2.urlopen(url)
        result = requested.read()
        r = json.loads(result)
        
        cast = r["credits"]["cast"]
        
        actor = []
        character = []
        for i in range (0, len(cast)):
            actor.append(cast[i]["name"])
            character.append(cast[i]["character"])

        button = request.form['button']
        if button == "Submit":
            status = "submitted"
            return render_template("results.html", status = status, character=character, actor=actor)
        else:
            status = "giveup"
            return render_template("results.html", status = status, character=character, actor=actor)
            

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
