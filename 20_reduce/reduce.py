'''
Team Zadical -- Zane Wang and Addison Huang
Softdev2 pd8
K20
2019-04-18
'''

from functools import reduce

book = open("utc.txt","r").read()
book = book.split(" ")


print(reduce((lambda x,y:x*y),[1,2,3,4]))

def wordFreq(word):
    return len([x for x in book if x == word])

print wordFreq("the")

print(reduce((lambda x,y:x=="hi" and y=="the"),["hi","the"]))
