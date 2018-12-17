import markovify
import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'blabberbot'))
import posified

class Blabberbot():
    def __init__(self,filepath):
        with open(filepath) as file:
            text = [line.strip() for line in file.readlines()]
        self.text_model = markovify.NewlineText(text)
        self.text_model_size = len(text)
    
    def add_corpus(self,filepath):
        with open(filepath) as file:
            text = [line.strip() for line in file.readlines()]
        new_model = markovify.NewlineText(text)
        corpus_size = len(text)
        if self.text_model_size > corpus_size:
            ratio1 = 1.0
            ratio2 = float(corpus_size)/float(self.text_model_size)
        else :
            ratio2 = 1.0
            ratio1 = float(self.text_model_size)/float(corpus_size)
        self.text_model = markovify.combine([self.text_model,new_model],[ratio1,ratio2])
    def generate_tweet(self,n):
        return self.text_model.make_short_sentence(n)

sheldon = "/home/fevenz/Sriram/Academic/Packages/Blabberbot/BlabberBot/Tweets/sheldonfinal.txt"
chandler = "/home/fevenz/Sriram/Academic/Packages/Blabberbot/BlabberBot/Tweets/chandlerfinal.txt"
