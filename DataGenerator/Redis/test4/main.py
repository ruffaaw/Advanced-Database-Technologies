import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

# Funkcja do pobierania wszystkich sesji dla danego użytkownika
def get_user_sessions(user_id):
    session_pattern = f"session:{user_id}:*"
    
    # Wyszukiwanie wszystkich kluczy sesji dla danego użytkownika
    session_keys = r.keys(session_pattern)
    
    user_sessions = {}
    for session_key in session_keys:
        session_id = session_key.decode().split(":")[2]
        exercise_pattern = f"{session_key.decode()}"
        exercise_keys = r.keys(exercise_pattern)
        
        exercises = []
        for exercise_key in exercise_keys:
            exercise_data = r.hgetall(exercise_key)
            exercises.append({
                "exercise_id": exercise_key.decode().split(":")[-1],
                "sets": int(exercise_data[b'sets'].decode()),
                "reps": int(exercise_data[b'reps'].decode()),
                "weight": int(exercise_data[b'weight'].decode())
            })
        
        user_sessions[session_id] = exercises
    
    return user_sessions

user_id = 1
start_time=time.time()
user_sessions = get_user_sessions(user_id)
end_time=time.time()
for session_id, exercises in user_sessions.items():
    print(f"Session ID: {session_id}")
    for exercise in exercises:
        print(f"  Exercise ID: {exercise['exercise_id']}, Sets: {exercise['sets']}, Reps: {exercise['reps']}, Weight: {exercise['weight']}")

print("Time: ", end_time-start_time, " s")