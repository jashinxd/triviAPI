from flask import Flask, render_template, Request
import urllib2, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/quiz")
def quiz():
    key = "bb8c8b5dede831baad7b87391d01d20c"
    uri = "https://api.themoviedb.org/3/movie/top_rated?api_key=%s"
    url = uri%(key)
    
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)

    topRated = []
    for item in r['results']:
        topRated.append(item['title'])

    #solely for aesthetic purposes to separate into two columbs
    firstHalf = []
    secondHalf = []
    count = 0
    for item in topRated:
        if count < 10:
            firstHalf.append(topRated[count])
        else:
            secondHalf.append(topRated[count])
        count += 1

    return render_template("quiz.html", firstTopMovies = firstHalf, secondTopMovies = secondHalf)

@app.route("/quiz/<movie>")

if __name__ == "__main__":
   app.debug = True
   app.run(host="0.0.0.0", port=8000)
