from flask import Flask, render_template
import urllib2, json

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"
    
