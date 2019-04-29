'''
Team Zadical -- Zane Wang and Addison Huang
Softdev2 pd8
K20
2019-04-29
'''

import re, functools

with open("utc.txt", "rU") as txt:
     text = txt.read()

def wordFreq(words):
    return len([x for x in range(0, len(text) - len(words)) if text[x: x + len(words)] == words])

words = re.findall(r'\w+', text)
phrase = list(set(word))

# this returns most frequent word in moby dick
def mostFreq():
    return functools.reduce(lambda a, b: a if a[1] > b[1] else b, [(x, words.count(x)) for x in phrase])


