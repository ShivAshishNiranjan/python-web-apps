__author__ = 'shiv_ashish_niranjan'

import pymongo

url = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(url)
database = client["sandb"]
collection = database["students"]

students = [student for student in collection.find({}) ]

print(students)
