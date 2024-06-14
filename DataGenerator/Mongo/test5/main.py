from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client['test']
users_collection = db['Users']

start_time=time.time()
for user_id in range(1, 11):
    user_id = str(user_id)
    new_password = f"password{user_id}"
    users_collection.update_one({f"_id": user_id}, {"$set": {"Password": new_password}})
end_time=time.time()
print("Time for 10: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 101):
    user_id = str(user_id)
    new_password = f"password{user_id}"
    users_collection.update_one({f"_id": user_id}, {"$set": {"Password": new_password}})
end_time=time.time()
print("Time for 100: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 1001):
    user_id = str(user_id)
    new_password = f"password{user_id}"
    users_collection.update_one({f"_id": user_id}, {"$set": {"Password": new_password}})
end_time=time.time()
print("Time for 1000: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 10001):
    user_id = str(user_id)
    new_password = f"password{user_id}"
    users_collection.update_one({f"_id": user_id}, {"$set": {"Password": new_password}})
end_time=time.time()
print("Time for 10000: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 100001):
    user_id = str(user_id)
    new_password = f"password{user_id}"
    users_collection.update_one({f"_id": user_id}, {"$set": {"Password": new_password}})
end_time=time.time()
print("Time for 100000: ", end_time-start_time, " s")

client.close()