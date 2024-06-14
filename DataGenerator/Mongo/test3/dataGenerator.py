from pymongo import MongoClient
from datetime import datetime, timedelta
import random

client = MongoClient('localhost', 27017)
db = client['test']
sessions_collection = db['Sessions']

def generate_session_data(user_id):
    date = datetime.now() - timedelta(days=random.randint(0, 365))  
    duration = random.randint(30, 120)  
    exercises = [
        {"exercise_id": 1, "sets": random.randint(1, 5), "reps": random.randint(5, 15), "weight": random.randint(5, 100)},
        {"exercise_id": 2, "sets": random.randint(1, 5), "reps": random.randint(5, 15), "weight": random.randint(5, 100)},
        {"exercise_id": 3, "sets": random.randint(1, 5), "reps": random.randint(5, 15), "weight": random.randint(5, 100)},
        {"exercise_id": 4, "sets": random.randint(1, 5), "reps": random.randint(5, 15), "weight": random.randint(5, 100)},
        {"exercise_id": 5, "sets": random.randint(1, 5), "reps": random.randint(5, 15), "weight": random.randint(5, 100)},
        {"exercise_id": 6, "sets": random.randint(1, 5), "reps": random.randint(5, 15), "weight": random.randint(5, 100)},
    ]
    return {"user_id": user_id, "date": date, "duration": duration, "exercises": exercises}

for user_id in range(1, 100001):  
    # for _ in range(200): 
        session_data = generate_session_data(1)
        sessions_collection.insert_one(session_data)
        if user_id%10000 == 0:
            print(user_id)

client.close()
