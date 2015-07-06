from pymongo import MongoClient
import random


client = MongoClient()

# get de database
db = client.abel

#get the collection
docs = db.documents

# insert a new doc
doc1 = dict(author="abel gonzalez", numpages=str(random.randint(10,100)), year="1999")
doc2 = dict(author="martin garcia", numpages=str(random.randint(10,100)), year="2011")
doc3 = dict(author="martin garcia", numpages=str(random.randint(10,100)), year="1999")

docs.save(doc1)
docs.save(doc2)
docs.save(doc3)

print list(docs.find())

docs.remove(dict(year="1999"))

print "***** ---> ", list(docs.find())

docs.remove() # remove'em all!!!
