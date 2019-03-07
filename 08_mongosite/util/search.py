import pymongo

SERVER_ADDR= "206.189.227.59"
connection = pymongo.MongoClient(SERVER_ADDR)
db = connection.test
collection = db.prize

def result(name):
    data=list(collection.find({"prizes.year":"2018"},{'_id': False}))
    parse=data[0]['prizes']
    output=[]
    for prizes in parse:
        for prize in prizes['laureates']:
            output.append(prize['firstname']+" "+prize['surname'])
    print(output)
    for i in output:
        if name==i:
            return name
    return False

def changeIp(ip):
    myclient = pymongo.MongoClient("mongodb://"+ip+":5000")
    db = myclient["test"]
    collection = db["prize"]

    with open('./static/prizes.json') as doc:
        file_data = json.load(doc)

    collection.insert(file_data)
    client.close()
    print("hi")
