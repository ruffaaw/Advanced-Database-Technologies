import sqlite3
import random
from datetime import datetime, timedelta
import time

conn = sqlite3.connect('C:\Studia\Magisterka\Semestr1\ZTBD\SQLite\gym.db')
cursor = conn.cursor()
# def generate_users(end_range):
#     time_start = time.time()
#     for i in range(end_range):
#         username = f"user{i}"
#         email = f"user{i}@example.com"
#         password = "password123"  
#         cursor.execute(
#             "INSERT INTO Users (Username, Email, Password) VALUES (?, ?, ?)",
#             (username, email, password)
#         )
#     conn.commit()
#     time_end = time.time()
#     print("Time for ", end_range, " ", time_end-time_start)
    
# generate_users(10)
# generate_users(100)
# generate_users(1000)
# generate_users(10000)
# generate_users(100000)
# conn.commit()

# Generowanie sesji treningowych
for i in range(1, 90001):
    # user_id = random.randint(1, 1000)  # Losowy identyfikator użytkownika
    user_id = 1
    date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')  # Losowa data w ciągu ostatniego roku
    duration = random.randint(30, 120)  # Losowy czas trwania treningu w minutach
    cursor.execute(
        "INSERT INTO Sessions (User_ID, Date, Duration) VALUES (?, ?, ?)",
        (user_id, date, duration)
    )

    # Zatwierdzenie transakcji co 10000 sesji
    if i % 10000 == 0:
        conn.commit()
        print(f"Inserted {i} sessions")

# Zatwierdzenie transakcji dla sesji treningowych
conn.commit()

# Zamknięcie połączenia
cursor.close()
conn.close()