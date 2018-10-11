Most of these project files were originally cloned from this [Udacity github repository](https://github.com/udacity/AIND-Recognizer). 
Udacity's README file is duplicated [here](README_Udacity.md).

## Method

The data used for this project were extracted from videos of ASL signers signing various words, and represent sequences of x and y coordinates of both hands (right/left, up/down). Each possible word usually has (well) more than one video sample to take into account variations over multiple occurrences and across different signers. An example of such a video sample can be seen [here](https://drive.google.com/file/d/0B_5qGuFe-wbhUXRuVnNZVnMtam8/view).

Each sign can be modeled as a sequence of unobservable states known as a [Hidden Markov Model (HMM)](https://en.wikipedia.org/wiki/Hidden_Markov_model). Each state produces different possible outputs that are observed (in this case, hand positions). Since the states are unobserved, it's not known how many there are, but with enough data the number of states that best fit the data can be determined.

So each word is assigned a separate HMM. The multiple coordinate sequences are used to train that word's HMM.

The best place to start understanding the structures of the code and the data, in my opinion, is [the notebook itself](asl_recognizer.ipynb). It is divided into three parts:

### Part 1
The student is familiarized with the data files in the [data](data) folder and the classes used in the code to load them in. 

The student also derives additional features for later testing. These are the feature sets I derived:

- _features_custom_n2g_: x/y coordinates with origin shifted to the signer's nose ("ground"), and [normalized](https://en.wikipedia.org/wiki/Standard_score)
- _features_custom_pn2g_: Same as "n2g" but in polar coordinates
- _features_custom_dn2g_: The delta between successive frames for the "n2g" numbers is taken
- _features_custom_n2g_dn2g_: The "n2g" and "dn2g" feature sets are combined

### Part 2

The student is shown how to use the hmmlearn library "GaussianHMM" class. The student then implements the Selector* classes in [my_model_selectors.py](my_model_selectors.py), particularly the "select" method. For a given word this method runs through each possible number of states, instantiates a GaussianHMM object according that number, and performs a fit on the selected features (i.e. the HMM is trained). The model is subsequently scored based on a criterion. Three Selector classes implement three different criteria:

1. CV: Log likehood with [k-fold cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)#k-fold_cross-validation)
1. BIC: [Bayesian Information Criterion](https://en.wikipedia.org/wiki/Bayesian_information_criterion)
1. DIC: [Discriminative Information Criterion](https://pdfs.semanticscholar.org/ed3d/7c4a5f607201f3848d4c02dd9ba17c791fc2.pdf)

The model with the best score is determined for the given word. Five such words are tested.

### Part 3

Optimal models are determined for all words in the training set. The student implements the "recognize" function in [my_recognizer.py](my_recognizer.py), which collects the best guess word and associated probabilities for every sequence of x/y coordinates in a test set of sentences. Multiple combinations of Selector type and feature set are tested; three of them are documented in the notebook.  A Word Error Rate (WER) for each combination. Conclusions are drawn.

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

It seemed that feature engineering had a greater impact than which selector was used, based on WER. For a given feature set the different selectors had similar WERs. The "n2g_dn2g" feature set that combined both spatial and temporal information performed the best, with a WER of slightly less than 50%. The high WER is attributed to the insufficiency of HMMs to capture all the characteristics of signs as they occur in sentences. An optional fourth section suggests the use of [statistical language models](https://en.wikipedia.org/wiki/Language_model) to improve the results.
