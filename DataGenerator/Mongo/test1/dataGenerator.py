import random
from pymongo import MongoClient
import time

exercise_descriptions = {
    "Squats": "Squats are a strength training exercise where an individual stands in an upright position then lowers their body down while maintaining balance and control until the thighs are parallel to the floor and then returns to the upright position, engaging the muscles of the legs, glutes, and back",
    "Bench Press": "Bench press is a popular strength training exercise where an individual lies on a bench and lifts a weighted barbell or dumbbells upward from the chest until the arms are fully extended and then lowers the weight back down to the chest, primarily targeting the muscles of the chest, shoulders, and arms",
    "Deadlifts": "Deadlifts involve lifting a barbell or weights from the floor to a standing position using a hip hinge movement pattern, targeting multiple muscle groups including the back, glutes, hamstrings, and core, effective for building overall strength and power",
    "Pull-ups": "Pull-ups are a bodyweight exercise where an individual hangs from a bar with an overhand grip and pulls their body upward until the chin is above the bar and then lowers back down with control, primarily working the muscles of the back, arms, and shoulders, effective for improving upper body strength and endurance",
    "Lunges": "Lunges are a lower body exercise where an individual steps forward with one leg and lowers their body until both knees are bent at a 90-degree angle and then returns to the starting position, targeting the muscles of the legs including the quadriceps, hamstrings, and glutes, also engaging the core for stability",
    "Planks": "Planks are a core-strengthening exercise where an individual holds a push-up position with the body in a straight line from head to heels supporting their weight on their forearms and toes, engaging the muscles of the core including the abdominals, obliques, and lower back, helping improve overall stability and posture"
}

client = MongoClient("mongodb://localhost:27017/")
db = client["test"]  
collection = db["Exercises"]  

def generate_exercises(end_range):
    start_time = time.time()
    bulk_operations = []
    for i in range(end_range):
        exercise_name = random.choice(list(exercise_descriptions.keys()))
        exercise_description = exercise_descriptions[exercise_name]
        data = {
            "name": exercise_name,
            "description": exercise_description
        }
        bulk_operations.append(data)

    collection.insert_many(bulk_operations)
    end_time = time.time()
    print("Time for ", end_range, " ", end_time-start_time, " s")
generate_exercises(10)
generate_exercises(100)
generate_exercises(1000)
generate_exercises(10000)
generate_exercises(100000)