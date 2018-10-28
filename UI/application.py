from flask import Flask, session , render_template ,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tweet" , methods=["POST"])
def tweet():
    try:
        celebrity = request.form.get("celebrity")
        print(celebrity)
    except ValueError:
        return render_template("error.html",error="Please select a celebrity")

    #TODO import Markov library enter the celeb and get the tweet

    return render_template("tweet.html" , tweet = tweet) 
