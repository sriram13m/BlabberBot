import sys
sys.path.insert(0, '/home/fevenz/Sriram/Projects/Packages/Blabberbot/BlabberBot/blabberbot/')
from flask import Flask, session , render_template ,request
import blabberbot

app = Flask(__name__)

@app.route("/")
def index():
    print(blabberbot.celebs)
    return render_template("index.html", celebrities = blabberbot.celebs)

@app.route("/tweet" , methods=["POST"])
def tweet():
    try:
        celebrity_name = request.form.get("celebrity")
        print(celebrity_name)
    except ValueError:
        return render_template("error.html",error="Please select a celebrity")

    engine = blabberbot.Blabberbot(blabberbot.celebs[celebrity_name])
    tweet = engine.make_sentences(140)

    return render_template("tweet.html" , tweet = tweet)
