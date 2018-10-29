import markovify

class Blabberbot():
    def __init__(self,filepath):
        with open(filepath) as file:
            text = file.read()
        self.text_model = markovify.Text(text)

    def make_sentences(self,n):
        return self.text_model.make_short_sentence(n)

textPath = "../Tweets/ElonMusk.txt"
celebs = {}
celebs["ElonMusk"] = "../Tweets/ElonMusk.txt"
celebs["Tesla"] = "../Tweets/Testa.txt"

engine = Blabberbot(textPath)
print(engine.make_sentences(140))
