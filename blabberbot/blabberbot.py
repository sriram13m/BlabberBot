import markovify
import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'blabberbot'))
import posified

class Blabberbot():
    def __init__(self,filepath):
        with open(filepath) as file:
            text = [line.strip() for line in file.readlines()]
        self.text_model = posified.POSifiedText(text)
    
    def add_corpus(self,filepath):
        with open(filepath) as file:
            text = [line.strip() for line in file.readlines()]
        new_model = posified.POSifiedText(text)
        self.text_model = markovify.combine([self.text_model,new_model])

    def generate_tweet(self,n):
        return self.text_model.make_short_sentence(n)

sheldon = "/app/Tweets/sheldonfinal.txt"
chandler = "/app/Tweets/chandlerfinal.txt"
