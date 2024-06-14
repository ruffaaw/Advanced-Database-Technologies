import pymongo
from datetime import datetime, timedelta
import random

# Połączenie z MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["test"]

# Kolekcje
users_collection = db["Users"]
exercises_collection = db["Exercises"]
workouts_collection = db["Workouts"]

# Przykładowi użytkownicy i ćwiczenia
users = list(users_collection.find())
exercises = list(exercises_collection.find())

# Funkcja generująca losowe ćwiczenia
def generate_random_exercises(num_exercises):
    random_exercises = random.sample(exercises, num_exercises)
    workout_exercises = []
    for exercise in random_exercises:
        workout_exercises.append({
            "exercise_id": exercise["_id"],
            "sets": random.randint(1, 5),
            "reps": random.randint(5, 15),
            "weight": random.uniform(10, 100)
        })
    return workout_exercises

# Generowanie danych dla kolekcji Workouts
num_workouts = 100  # Liczba treningów do wygenerowania
for _ in range(num_workouts):
    user = random.choice(users)
    workout = {
        "user_id": user["_id"],
        "date": datetime.now() - timedelta(days=random.randint(0, 365)),
        "exercises": generate_random_exercises(random.randint(1, 5))
    }
    workouts_collection.insert_one(workout)

print("Dane zostały pomyślnie dodane do kolekcji Workouts.")
