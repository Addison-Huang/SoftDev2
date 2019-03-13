from pymongo import MongoClient
import json

SERVER_ADDR= "206.189.227.59"
client = MongoClient(SERVER_ADDR, 27017)
db = client.test
collection = db.prize

def result(name):
    data=list(collection.find({"prizes.year":"2018"},{'_id': False}))
    parse=data[0]['prizes']
    output=[]
    for prizes in parse:
        for prize in prizes['laureates']:
            output.append(prize['firstname']+" "+prize['surname'])
    for i in output:
        if name==i:
            return name
    return False

def changeIp(ip):
    SERVER_ADDR=ip
    myclient = MongoClient(SERVER_ADDR)
    with open('./data/prizes.json') as doc:
        file_data = json.load(doc)
        print(file_data)
        #client.drop_database("prize")
        mydb = myclient["test"]
        col = mydb["prize"]
        print('hi1')
        col.insert_many(file_data)
        print('hi2')
