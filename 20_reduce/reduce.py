'''
Team Zadical -- Zane Wang and Addison Huang
Softdev2 pd8
K20
2019-04-18
'''

import re
from functools import reduce
punctuation = "!@#$%^&*(),./;'\" "

book = open("utc.txt","r").read()
book = book.lower()
bookL = re.findall(r'\w+', book)
book = " ".join(bookL)
test = ["the", "the", "hi", "the","the", "and", "the","hi","the","the"]

def wordFreq(word):
    return len([x for x in book if x == word])

print wordFreq("the")

#print(reduce((lambda x,y:x=="hi" and y=="the"),["hi","the"]))

def groupFreq(phrase):
    words = phrase.split(" ")
    counter = 0
    amount = 0
    for x in test:
        if x == words[0]:
            y = test[counter:counter+len(words)]
            if y == words:
              amount +=1
        counter += 1
    return amount

print(groupFreq("the the"))

def phraseFreq(phrase):
    return len([x for x in range(0, len(book) - len(phrase)) if book[x:x + len(phrase)] == phrase])

print(phraseFreq("there"))

                
        
