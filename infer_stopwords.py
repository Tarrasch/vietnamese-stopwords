import sys
import itertools


with open(sys.argv[1], 'r') as my_file:
    stopwords = {word.strip() for word in my_file.read().split('\n')}
with open(sys.argv[2], 'r') as my_file:
    all_words = {word.strip() for word in my_file.read().split('\n')}

potential_stopwords = {w1 + "_" + w2 for (w1, w2) in
                       itertools.product(stopwords, repeat=2)}
potential_stopwords &= all_words
potential_stopwords -= stopwords
print('\n'.join(sorted(list(potential_stopwords))))
