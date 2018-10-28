from flask import Flask, session , render_template ,request
#import blabberbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", celebrity = celebrity)

@app.route("/tweet" , methods=["POST"])
def tweet():
    try:
        celebrity_name = request.form.get("celebrity")
        print(celebrity_name)
    except ValueError:
        return render_template("error.html",error="Please select a celebrity")

    #TODO import Markov library enter the celeb and get the tweet

    return render_template("tweet.html" , tweet = tweet)
