import redis
import random
import datetime
import time
time_limit = 6 * 30 * 24 * 60 * 60  # 6 months in seconds

r = redis.Redis(host='localhost', port=6379, db=0)

current_time = int(time.time())
start_time = time.time()
sessions=[]
for key in r.scan_iter(match="session:*", count=None):
    sessions.append(key)
for session_key in sessions:
    session_timestamp = r.hget(session_key, "date")
    session_timestamp = session_timestamp.decode("utf-8")
    session_timestamp = datetime.datetime.strptime(session_timestamp, '%Y-%m-%d').timestamp()
    if session_timestamp is None:
        continue

    session_age = current_time - int(session_timestamp)
    if session_age > time_limit:
        print(session_key)
        r.delete(session_key)

end_time = time.time()
print("Time for deleting ", end_time-start_time, " s")