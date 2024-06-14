import redis
import random
from datetime import datetime, timedelta

# Połączenie z serwerem Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Funkcja do generowania danych sesji treningowych
def generate_session_data(user_id):
    sessions = []
    current_date = datetime.now()
    for i in range(100000):  # Dodaj 200 sesji dla każdego użytkownika
        session_date = current_date - timedelta(days=random.randint(0, 365))  # Losowa data w ciągu ostatniego roku
        duration = random.randint(30, 120)  # Losowy czas trwania sesji w minutach
        session_key = f"session_data:{user_id}:{i+1}"
        r.hmset(session_key, {
            "date": session_date.strftime('%Y-%m-%d'),
            "duration": duration
        })
    print(f"Dane sesji treningowych dla użytkownika {user_id} zostały dodane do Redis.")

# Dodawanie danych sesji treningowych do Redis dla 1000 użytkowników
generate_session_data(1)
