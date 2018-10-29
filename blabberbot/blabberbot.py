import markovify

class Blabberbot():
    def __init__(self,filepath):
        with open(filepath) as file:
            text = [line.decode('utf-8').strip() for line in file.readlines()]
            #text = file.read()
        self.text_model = markovify.Text(text)

    def make_sentences(self,n):
        return self.text_model.make_short_sentence(n)

celebs = {}
celebs["ElonMusk"] = "../Tweets/ElonMusk.txt"
celebs["Tesla"] = "../Tweets/Tesla.txt"
