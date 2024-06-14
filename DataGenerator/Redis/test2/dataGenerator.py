import redis
from datetime import datetime, timedelta

# Połączenie z serwerem Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Funkcja do dodawania sesji treningowej
def add_training_session(user_id, date, duration):
    session_data = {
        'user_id': user_id,
        'date': date.strftime('%Y-%m-%d'),
        'duration': duration
    }
    r.lpush('training_sessions', session_data)

# Funkcja do pobierania sesji treningowych dla danego użytkownika z ostatnich 7 dni
def get_recent_training_sessions(user_id):
    start_date = datetime.now() - timedelta(days=7)
    training_sessions = r.lrange('training_sessions', 0, -1)
    recent_sessions = []
    for session in training_sessions:
        session_data = eval(session)
        if session_data['user_id'] == user_id and datetime.strptime(session_data['date'], '%Y-%m-%d') >= start_date:
            recent_sessions.append(session_data)
    return recent_sessions

# Dodanie przykładowych sesji treningowych
add_training_session(1, datetime(2024, 4, 1), 60)
add_training_session(2, datetime(2024, 4, 3), 45)
add_training_session(1, datetime(2024, 4, 5), 90)
add_training_session(3, datetime(2024, 4, 7), 30)

# Pobranie sesji treningowych dla użytkownika 1 z ostatnich 7 dni
user_id = 1
recent_sessions = get_recent_training_sessions(user_id)
print("Recent training sessions for user", user_id)
for session in recent_sessions:
    print(session)
