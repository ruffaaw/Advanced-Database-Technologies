import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

def calculate_average_load_per_user():
    user_exercise_load = {}

    for key in r.scan_iter(match="session:*:exercise:*"):
        exercise_data = r.hgetall(key)
        user_id, session_id, xd, exercise_id = key.decode().split(":")[1:5]
        user_id = int(user_id)
        exercise_id = int(exercise_id)
        sets = int(exercise_data[b'sets'].decode())
        reps = int(exercise_data[b'reps'].decode())
        weight = int(exercise_data[b'weight'].decode())

        exercise_load = sets * reps * weight

        if user_id not in user_exercise_load:
            user_exercise_load[user_id] = {}
        if exercise_id not in user_exercise_load[user_id]:
            user_exercise_load[user_id][exercise_id] = []
        user_exercise_load[user_id][exercise_id].append(exercise_load)

    average_load_per_user = {}
    for user_id, exercises in user_exercise_load.items():
        average_load_per_user[user_id] = {}
        for exercise_id, loads in exercises.items():
            average_load_per_user[user_id][exercise_id] = sum(loads) / len(loads)

    return average_load_per_user

time_start = time.time()
average_load_per_user = calculate_average_load_per_user()
time_stop = time.time()
print("Średnie obciążenie każdego użytkownika na poszczególnych ćwiczeniach:")
for user_id, exercises in average_load_per_user.items():
    print(f"Użytkownik {user_id}:")
    for exercise_id, load in exercises.items():
        print(f"    Ćwiczenie {exercise_id}: Średnie obciążenie {load}")
print("Czas wykonania zadania:", time_stop-time_start)