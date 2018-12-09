BlabberBot:
    BlabberBot is a Twitter Bot Generator based on Markov Chain.
    It is described here
    An 24/7 Twitter Bot created using BlabberBot that mimics ElonMusk has been deployed via Heroku.(It can be found here)
Dependencies:
    The bot is implemented using Python 3.5.3.
    Various libraries such as Tweepy,markovify,flask has been used.
    You can install them manually or simply do pip install -r requirements.txt
Usage:
    Twitter Bot:
        To set up a Twitter Bot you'll need a Twitter Account and a Twitter application. From the latter, you'll need a consumer key, a consumer secret, an access token and an access token secret.

        Enter these in credentials.py which is to be placed at Tweets folder
        The file should look like this:

        CONSUMER_KEY = 'consumer key'
        CONSUMER_SECRET = 'consumer secret'
        ACCESS_KEY = 'access key'
        ACCESS_SECRET = 'access secret'

        After finishing the setup, run python3 tweet.py to activate the Twitter Bot.

    Web Based User Interface:
        To set up the Web User Interface, make sure you have flask installed. To setup flask you'll need to export FLASK_APP=application.py in the environment. After that a simple flask run will render the Web Based UI. A Minimalistic UI is been implemented here. You can extend it by adding further HTML and CSS files.
