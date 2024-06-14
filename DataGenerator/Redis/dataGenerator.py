import redis
import random
import time

r = redis.Redis(host='localhost', port=6379, db=0)

exercise_descriptions = {
    "Squats": "Squats are a strength training exercise where an individual stands in an upright position then lowers their body down while maintaining balance and control until the thighs are parallel to the floor and then returns to the upright position, engaging the muscles of the legs, glutes, and back",
    "Bench Press": "Bench press is a popular strength training exercise where an individual lies on a bench and lifts a weighted barbell or dumbbells upward from the chest until the arms are fully extended and then lowers the weight back down to the chest, primarily targeting the muscles of the chest, shoulders, and arms",
    "Deadlifts": "Deadlifts involve lifting a barbell or weights from the floor to a standing position using a hip hinge movement pattern, targeting multiple muscle groups including the back, glutes, hamstrings, and core, effective for building overall strength and power",
    "Pull-ups": "Pull-ups are a bodyweight exercise where an individual hangs from a bar with an overhand grip and pulls their body upward until the chin is above the bar and then lowers back down with control, primarily working the muscles of the back, arms, and shoulders, effective for improving upper body strength and endurance",
    "Lunges": "Lunges are a lower body exercise where an individual steps forward with one leg and lowers their body until both knees are bent at a 90-degree angle and then returns to the starting position, targeting the muscles of the legs including the quadriceps, hamstrings, and glutes, also engaging the core for stability",
    "Planks": "Planks are a core-strengthening exercise where an individual holds a push-up position with the body in a straight line from head to heels supporting their weight on their forearms and toes, engaging the muscles of the core including the abdominals, obliques, and lower back, helping improve overall stability and posture"
}
all_time=0
for i in range(1, 1000001):
    exercise_name = random.choice(list(exercise_descriptions.keys()))
    exercise_description = exercise_descriptions[exercise_name]
    redis_key = f"exercise:{i}"
    start_time = time.time()
    r.hset(redis_key, "name", exercise_name)
    r.hset(redis_key, "description", exercise_description)
    end_time = time.time()
    all_time+= end_time-start_time
minutes = int(all_time // 60)
seconds = int(all_time % 60)
milliseconds = int((all_time - int(all_time)) * 1000)
print(f"{minutes} min {seconds} sek {milliseconds} ms")
# import redis
# import random
# import json

# # Połączenie z serwerem Redis
# r = redis.Redis(host='localhost', port=6379, db=0)

# # Opisy ćwiczeń
# exercise_descriptions = {
#     "Squats": "Squats are a strength training exercise where an individual stands in an upright position then lowers their body down while maintaining balance and control until the thighs are parallel to the floor and then returns to the upright position, engaging the muscles of the legs, glutes, and back",
#     "Bench Press": "Bench press is a popular strength training exercise where an individual lies on a bench and lifts a weighted barbell or dumbbells upward from the chest until the arms are fully extended and then lowers the weight back down to the chest, primarily targeting the muscles of the chest, shoulders, and arms",
#     "Deadlifts": "Deadlifts involve lifting a barbell or weights from the floor to a standing position using a hip hinge movement pattern, targeting multiple muscle groups including the back, glutes, hamstrings, and core, effective for building overall strength and power",
#     "Pull-ups": "Pull-ups are a bodyweight exercise where an individual hangs from a bar with an overhand grip and pulls their body upward until the chin is above the bar and then lowers back down with control, primarily working the muscles of the back, arms, and shoulders, effective for improving upper body strength and endurance",
#     "Lunges": "Lunges are a lower body exercise where an individual steps forward with one leg and lowers their body until both knees are bent at a 90-degree angle and then returns to the starting position, targeting the muscles of the legs including the quadriceps, hamstrings, and glutes, also engaging the core for stability",
#     "Planks": "Planks are a core-strengthening exercise where an individual holds a push-up position with the body in a straight line from head to heels supporting their weight on their forearms and toes, engaging the muscles of the core including the abdominals, obliques, and lower back, helping improve overall stability and posture"
# }

# # Generowanie danych i wstawianie ich do kolekcji w formie listy w Redis
# exercises_collection = "exercises_collection"
# for i in range(1, 10001):
#     exercise_name = random.choice(list(exercise_descriptions.keys()))
#     exercise_description = exercise_descriptions[exercise_name]
#     exercise_data = {"id": i, "name": exercise_name, "description": exercise_description}
#     r.rpush(exercises_collection, json.dumps(exercise_data))
