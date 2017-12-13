import game_framework
import title_state
from pico2d import *

class Entry:
    def __init__(self, score, time):
        self.score = score
        self time = time

name = "ScoreState"
usesPickle = True
if (usesPickle):
    fileName = "score.pickle"
else:
    fileName = "score.json"

def loadScores():
    global scores
    scores = []
    if(usesPickle):
        f = open(filename,"rb")
        scores = pickle.load(f)
        f.close
    # load scores from disk

def saveScores():
    if (usesPickle):
        f = open(fileName, "w")
        pickle.dump(scores.f)
        f.close()

def add(score):
        scores.append(score)
        print("Now scores has" + str(len(scores)) + "entries.")
        saveScore()

    def enter():
        print("Now ScoreState")
        pass

    def exit():
        print ("Leaves ScoreState")


#    def handle_events(frame_time)
#        for event in events:
#            if event.type == SDL_QUIT:
#                game_framework
