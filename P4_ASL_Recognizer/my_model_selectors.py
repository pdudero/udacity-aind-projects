import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Bayesian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on BIC scores
        #print("SelectorBIC training on {} sequences for word {}".format(len(self.sequences),self.this_word))
        
        scoresary = np.full(self.max_n_components+1,np.PINF)
        for nstates in range(self.min_n_components,self.max_n_components+1):
            model = self.base_model(num_states=nstates)
            if (model != None):
                try:
                    logL = model.score(self.X, self.lengths)
                except:
                    print("Couldn't score model for word {} Nstates {}".format(self.this_word, nstates))
                else:
                    #Next three lines calculating BIC pulled from forum posts
                    logN = np.log(len(self.X))
                    nfreepar = nstates**2 + 2*nstates * model.n_features - 1
                    BIC = -2 * logL + nfreepar * logN
                    scoresary[nstates-1] = BIC
                    #print("Word {} Nstates {} BIC {}".format(self.this_word, nstates, BIC))

        bestnstates = np.argmin(scoresary)+1
        
        print("SelectorBIC trained on {} sequences for word {}, bestnstates={}, score={}".format(len(self.sequences),self.this_word, bestnstates, np.min(scoresary)))

        return self.base_model(bestnstates)


class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on DIC scores
        #print("SelectorDIC training on {} sequences for word {}".format(len(self.sequences),self.this_word))
        
        scoresary = np.full(self.max_n_components+1,np.NINF)
        for nstates in range(self.min_n_components,self.max_n_components+1):
            model = self.base_model(num_states=nstates)
            if (model != None):
                try:
                    logL = model.score(self.X, self.lengths)
                except:
                    print("Couldn't score model for word {} Nstates {}".format(self.this_word, nstates))
                else:
                    scores = []
                    for word in self.words.keys():
                        if word != self.this_word:
                            X, lengths = self.hwords[word]
                            try:
                                scores.append(model.score(X, lengths))
                            except:
                                print("Couldn't score model for word {} Nstates {}".format(word, nstates))
                                continue
                    if len(scores):
                        score = sum(scores)/len(scores)
                        DIC = logL - score
                        scoresary[nstates-1] = DIC
                        #print("Word {} Nstates {} DIC {}".format(self.this_word, nstates, DIC))

        bestnstates = np.argmax(scoresary)+1
        
        print("SelectorDIC trained on {} sequences for word {}, bestnstates={}, score={}".format(len(self.sequences),self.this_word, bestnstates, np.max(scoresary)))
        
        return self.base_model(bestnstates)



class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        
        if (len(self.sequences)<2):
            print("Can't perform SelectorCV.select() with less than 2 sequences, word {}".format(self.this_word))
            return None

        #print("SelectorCV training on {} sequences for word {}".format(len(self.sequences),self.this_word))
        
        saveX, savelengths = self.X, self.lengths
        
        # TODO implement model selection using CV
        scoresary = np.full(self.max_n_components+1,np.NINF)
        for nstates in range(self.min_n_components,self.max_n_components+1):
            split_method = KFold(n_splits = min(3,len(self.sequences)))
            scores = []
            for cv_train_idx, cv_test_idx in split_method.split(self.sequences):
                # view indices of the folds
                #print("Train fold indices:{} Test fold indices:{}".format(cv_train_idx, cv_test_idx))
                trainX, trainlengths = combine_sequences(cv_train_idx,self.sequences)
                testX, testlengths   = combine_sequences(cv_test_idx,self.sequences)
                self.X, self.lengths = trainX, trainlengths
                model = self.base_model(num_states=nstates)
                if (model != None):
                    try:
                        logL = model.score(testX, testlengths)
                    except:
                        print("Couldn't score model for word {} Nstates {}".format(self.this_word, nstates))
                    else:
                        scores.append(logL)
            if len(scores):
                scoresary[nstates-1] = sum(scores)/len(scores)
                #print("Word {} Nstates {} avg score {}".format(self.this_word, nstates, scoresary[nstates-1]))

        bestnstates = np.argmax(scoresary)+1

        print("SelectorCV trained on {} sequences for word {}, bestnstates={}, avg score={}".format(len(self.sequences),self.this_word, bestnstates, np.max(scoresary)))
        
        self.X, self.lengths = saveX, savelengths
       
        return self.base_model(bestnstates)
