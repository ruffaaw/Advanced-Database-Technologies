from pymongo import MongoClient
import time
import json

client = MongoClient('mongodb://localhost:27017')
db = client['test']
collection=db['Exercises']

with open("insert_queries_mongodb10.json","r") as file:
  data = json.load(file)

start_time=time.time()
collection.insert_many(data)
end_time=time.time()
minutes = int((end_time-start_time) // 60)
seconds = int((end_time-start_time) % 60)
milliseconds = int(((end_time-start_time) - int(end_time-(start_time))) * 1000)
print(f"{minutes} min {seconds} sek {milliseconds} ms")