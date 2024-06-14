import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

def delete_sessions_in_batches(batch_size):
    start_time = time.time()
    
    session_keys = []
    for key in r.scan_iter(match='session:*:exercise:*', count=100):
        session_keys.append(key)
        if len(session_keys) >= batch_size:
            break
    
    if session_keys:
        r.delete(*session_keys)
    
    end_time = time.time()
    print(f"Time for deleting {batch_size} sessions: ", end_time - start_time, " s")

delete_sessions_in_batches(10)
delete_sessions_in_batches(100)
delete_sessions_in_batches(1000)
delete_sessions_in_batches(10000)
delete_sessions_in_batches(100000)
