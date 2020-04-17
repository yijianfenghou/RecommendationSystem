from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np
import math
import collections
import random
from six.moves import xrange

local_file = "../data/trans_all_incode.csv"
log_dir = "./log"

def read_data(filename):
    corpus = []
    vocabulary = set()
    words = []
    max_len = 0
    with open(filename, "r") as f:
        for line in f:
            sentence = line.strip().split("|")
            corpus.append(sentence)
            max_len = max(max_len, len(sentence))
            words += sentence
    print('corpus size: %s sentence %s words'%(len(corpus), len(words)))
    print('sentence max len: %s'%(max_len))
    return corpus, words

def generate_batch_from_sentence(sentence, num_skips, skip_window):
    batch_inputs = []
    batch_labels = []
    for i in range(len(sentence)):
        window = list(range(len(sentence)))
        window.remove(i)
        sample_index = random.sample(window,min(num_skips, len(window)))
        input_id = word2id.get()

if __name__ == "__main__":
    corpus, words = read_data(local_file)
    vocabulary = collections.Counter(words)
    count = []
    count.extend(collections.Counter(words))
