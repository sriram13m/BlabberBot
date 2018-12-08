import markovify
from pathlib import Path
class Blabberbot():
    def __init__(self,filepath):
        with open(filepath) as file:
            text = [line.strip() for line in file.readlines()]
            #text = file.read()
        self.text_model = markovify.Text(text)

    def generate_tweet(self,n):
        return self.text_model.make_short_sentence(n)

folder = Path.cwd().parent / "Tweets"

celebs = {}
celebs["ElonMusk"] = folder / "ElonMusk.txt"
celebs["Tesla"] = folder / "Tesla.txt"
