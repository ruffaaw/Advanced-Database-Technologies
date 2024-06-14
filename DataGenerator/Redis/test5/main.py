import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

exercise_key = "session:1:1:exercise:1"

new_sets_value = 5  # Przykładowa nowa wartość
new_reps = 10
new_weight = 60

start_time=time.time()
r.hset(exercise_key, "sets", new_sets_value)
r.hset(exercise_key, "reps", new_reps)
r.hset(exercise_key, "weight", new_weight)
end_time=time.time()
print("Time: ", end_time-start_time, " s")