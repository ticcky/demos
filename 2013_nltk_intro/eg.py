#!/usr/bin/env python
#
# Essay Generator (NLTK demo)
# Author: Lukas Zilka
#
import nltk
import sys
import matplotlib.pyplot as plt


def generate_essay(file_name):
    # load text from our input file
    with open(file_name) as f_in:
        text = f_in.read()

    # have nltk tokenize it on whitespaces
    words = nltk.WhitespaceTokenizer().tokenize(text)
    # word = ['this', 'is', 'my', 'essay', ...]
    
    fd = nltk.FreqDist(words)  # count the word occurances

    # let's see if Zipf's law is really a law... let's plot
    ranks = []  # x axis
    freqs = []  # y axis
    for rank, word in enumerate(fd):
        ranks.append(rank)
        freqs.append(fd[word])
    
    plt.plot(ranks, freqs)  # standard plot
    plt.show()  # pop a gui window with the plot

    plt.loglog(ranks, freqs)  # log x and log y axis
    plt.show()

    # now let's get back to our essay generation

    # try generating the essay using only unigrams
    pd = nltk.MLEProbDist(fd)  # create maximum likelihood probability
                               # distribution based on the counts

    # try to generate the essay
    for i in range(250):
        print pd.generate(),
    print

    # the essay doesn't look good

    # let's try to use bigram model

    # ConditionalFreqDist accepts a list of tuples in a form (condition, value)
    # to build a frequency distribution; this suits our bigram model
    cfd = nltk.ConditionalFreqDist(nltk.bigrams(words))
    cpd = nltk.ConditionalProbDist(cfd, nltk.MLEProbDist)

    # let's generate using our bigram model
    word = "because"
    for i in range(250):
        print word,
        word = cpd[word].generate()


def print_help():
    print "Usage: {name} [file with previous essays compilation]".format(name=sys.argv[0])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        generate_essay(file_name)
    else:
        print_help()

