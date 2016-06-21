#!/usr/bin/env python3
# encoding: utf-8
 
import sys

from copy import deepcopy
from pprint import pprint
from random import choice
 
EOS = ['.', '?', '!', '...']
 
 
def build_dict(words):
    """
    Build a dictionary from the words.
 
    (word1, word2) => [w1, w2, ...]  # key: tuple; value: list
    """
    d = {}
    for i, word in enumerate(words):
        try:
            first, second, third = words[i], words[i+1], words[i+2]
        except IndexError:
            break
        key = (first, second)
        if key not in d:
            d[key] = []
        #
        d[key].append(third)
 
    return d
 
 
def generate_sentence(d):
    li = [key for key in d.keys() if key[0][0].isupper()]
    key = choice(li)
 
    li = []
    first, second = key
    li.append(first)
    li.append(second)
    while True:
        try:
            third = choice(d[key])
        except KeyError:
            break
        li.append(third)
        if third[-1] in EOS:
            break
        # else
        key = (second, third)
        first, second = key
 
    return ' '.join(li)
 
 
def main():
    keyword = []
    count = []
    copy = []
    users = []
    j =0
    k = 0

    fname = sys.argv[1]
    with open(fname, "rt", encoding="utf-8") as f:
        text = f.read()
    for i in range (0,5):
        key = input()
        keyword.insert(i, key)
        count.insert(i, 0)
    print("rrr")
    tweets = text.split(".*.")
    for tweet in tweets:
        words = tweet.split(" ") 
        for w in words:
            for r in range(0,5):
                if w == keyword[r]:
                    count[r] = count[r] + 1                         # Now I have all the number of search results
        copy = deepcopy(count)
        users.append(copy)
        print(copy)
        for i in range (0, 5):
            count[i] = 0

    for u in users:
        for i in u:
            k = k + i
        if (k >= 3):
            print(tweets[users.index(u)])
        k = 0
        #print(u)
    d = build_dict(words)
    pprint(d)
    print()
    sent = generate_sentence(d)
    print(sent)
    if sent in text:
       print('# existing sentence :(')
 
####################
 
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Error: provide an input corpus file.")
        sys.exit(1)
    else:
    	main()
