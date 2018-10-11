Most of these project files were originally cloned from this [Udacity github repository](https://github.com/udacity/AIND-Recognizer). 
Udacity's README file is duplicated [here](README_Udacity.md).

## Method

The data used for this project were extracted from videos of ASL signers signing various words, and represent sequences of x and y coordinates of both hands (right/left, up/down). Each possible word usually has (well) more than one video sample to take into account variations over multiple occurrences and across different signers. An example of such a video sample can be seen [here](https://drive.google.com/file/d/0B_5qGuFe-wbhUXRuVnNZVnMtam8/view).

Each sign can be modeled as a sequence of unobservable states known as a [Hidden Markov Model (HMM)](https://en.wikipedia.org/wiki/Hidden_Markov_model). Each state produces different possible outputs that are observed (in this case, hand positions). Since the states are unobserved, it's not known how many there are, but with enough data the number of states that best fit the data can be determined.

So each word is assigned a separate HMM. The multiple coordinate sequences are used to train that word's HMM.

The best place to start understanding the structures of the code and the data, in my opinion, is [the notebook itself](asl_recognizer.ipynb). It is divided into three parts:

### Part 1
The student is familiarized with the data files in the [data](data) folder and the classes used in the code to load them in. 

The student also derives additional features for later testing.

### Part 2

Students are shown how to use the hmmlearn library "GaussianHMM" class. Students then implement the Selector* classes in [my_model_selectors.py](my_model_selectors.py), particularly the "select" method. For a given word this method runs through each possible number of states, instantiates a GaussianHMM object according that number, and performs a fit on the selected features (i.e. the HMM is trained). The model is subsequently scored based on a criterion. Three Selector classes implement three different criteria:

1. CV: Log likehood with [k-fold cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)#k-fold_cross-validation)
1. BIC: [Bayesian Information Criterion](https://en.wikipedia.org/wiki/Bayesian_information_criterion)
1. DIC: [Discriminative Information Criterion](https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf)

The model with the best score is determined for the given word.

### Part 3



A description of the files in this repository follows:

Notes | File | Usage
--- |  --- | ---
[1] | [asl_recognizer.ipynb](asl_recognizer.ipynb) | Main notebook
[1] | [my_model_selectors.py](my_model_selectors.py) | Classes and functions that select the optimal number of states in an HMM based on various criteria
[1] | [my_recognizer.py](my_recognizer.py) | contains function "recognize" implemented by the student and used for part 3 in the notebook
[2] | [asl_data.py](asl_data.py) | Provides classes and utility functions that read csv files from the [data](data) folder, using [pandas](https://pandas.pydata.org/) dataframes, and formats it in a manner suitable for use with the [hmmlearn](https://hmmlearn.readthedocs.io/) library 
[2] | [asl_test_model_selectors.py](asl_test_model_selectors.py) | unit tests for [my_model_selectors.py](my_model_selectors.py)
[2] | [asl_test_recognizer.py](asl_test_recognizer.py) | unit tests for [my_recognizer.py](my_recognizer.py)
[2] | [asl_utils.py](asl_utils.py) | Miscellaneous utilities

- [1] Implemented by the student using supplied sample/skeleton code
- [2] Supplied


## Results
