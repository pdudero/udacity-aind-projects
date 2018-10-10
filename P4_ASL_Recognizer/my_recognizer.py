import warnings
from asl_data import SinglesData
import numpy as np

def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

   :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
   :param test_set: SinglesData object
   :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
   """
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    probabilities = []
    guesses = []
    # TODO implement the recognizer
    # return probabilities, guesses
    for i in range(len(test_set.df)):
        probdict = {}
        maxscore = np.NINF
        bestword = ''
        # test against the words in the models dict
        for word,model in models.items():
            try:
                X, lengths = test_set.get_item_Xlengths(i)
                score = model.score(X, lengths)
            except:
                pass
                #print("Couldn't score model for word {}".format(word))
            else:
                probdict[word] = score
                if (score>maxscore):
                    maxscore = score
                    bestword = word
        probabilities.append(probdict)
        guesses.append(bestword)
    return probabilities, guesses
