import redis
from datetime import datetime, timedelta
import time

# Połączenie z serwerem Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def calculate_weekly_gym_time():
    total_time = {}
    one_week_ago = datetime.now() - timedelta(days=7)
    
    session_keys = r.keys("session_data:*")
    for session_key in session_keys:
        session_data = r.hgetall(session_key)
        session_date_str = session_data[b'date'].decode('utf-8')
        session_date = datetime.strptime(session_date_str, '%Y-%m-%d')
        session_duration = int(session_data[b'duration'].decode('utf-8'))
        
        if session_date >= one_week_ago:
            parts = session_key.decode('utf-8').split(':')
            user_id = parts[1]
            if user_id not in total_time:
                total_time[user_id] = 0
            total_time[user_id] += session_duration
    
    return total_time

start_time = time.time()
weekly_gym_time = calculate_weekly_gym_time()
end_time = time.time()
print("Total time for 100000: ", end_time-start_time, " s")