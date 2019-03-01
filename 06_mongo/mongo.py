'''
Team Apple Wine -- Johnny and Addison
SoftDev2 pd8
K#06 --Yummy Mongo Py
2019-03-01
'''

import pymongo

SERVER_ADDR="lisa.stuy.edu"
connection = pymongo.MongoClient(SERVER_ADDR)
db=connection.test
collection = db.restaurants

def find_borough(borough):
    print(collection.find({"borough":borough}))


def find_zip(zipcode):
    print(collection.find({"address.zipcode":str(zipcode)}))


def find_zip_grade(zipcode,grade):
    print(collection.find({"$and":[{"address.zipcode":str(zipcode)}, {"grades.grade":grade}]}))


def find_zip_score(zipcode,score):
    print(collection.find({"$and":[{"address.zipcode":str(zipcode)}, {"grades.score":{"$lt":score}}]}))




