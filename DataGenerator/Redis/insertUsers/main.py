import redis
from datetime import datetime, timedelta
import time

r = redis.Redis(host='localhost', port=6379, db=0)

start_time=time.time()
for i in range(1, 11):
  user_key = f"user:{i}"
  r.hset(user_key, "Password", f"password")
end_time=time.time()
print("Time for 10: ", end_time-start_time, " s")

start_time=time.time()
for i in range(11, 112):
  user_key = f"user:{i}"
  r.hset(user_key, "Password", f"password")
end_time=time.time()
print("Time for 100: ", end_time-start_time, " s")

start_time=time.time()
for i in range(112, 1113):
  user_key = f"user:{i}"
  r.hset(user_key, "Password", f"password")
end_time=time.time()
print("Time for 1000: ", end_time-start_time, " s")

start_time=time.time()
for i in range(1113, 11114):
  user_key = f"user:{i}"
  r.hset(user_key, "Password", f"password")
end_time=time.time()
print("Time for 10000: ", end_time-start_time, " s")

start_time=time.time()
for i in range(11114, 111115):
  user_key = f"user:{i}"
  r.hset(user_key, "Password", f"password")
end_time=time.time()
print("Time for 100000: ", end_time-start_time, " s")
