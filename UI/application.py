import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'blabberbot'))
from flask import Flask, session , render_template ,request
import blabberbot

app = Flask(__name__)

@app.route("/")
def index():
    #print(blabberbot.celebs)
    return render_template("index.html", celebrities = blabberbot.celebs.keys())

@app.route("/tweet" , methods=["POST"])
def tweet():
    try:
        celebrity_name = request.form.get("celebrity")
        #print(celebrity_name)
    except KeyError:
        return render_template("error.html",error="Please select a celebrity")

    if celebrity_name not in blabberbot.celebs.keys():
        return render_template("error.html",error="Please select a celebrity")
    engine = blabberbot.Blabberbot(blabberbot.celebs[celebrity_name])
    tweet = engine.generate_tweet(140)
    #print(tweet)

    return render_template("tweet.html" , tweet = tweet)
