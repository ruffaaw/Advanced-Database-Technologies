import psycopg2
from psycopg2 import sql
import random
from datetime import datetime, timedelta
import time

conn = psycopg2.connect(
    dbname="gyms",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# def generate_users(end_range):
#     time_start = time.time()
#     for i in range(end_range):
#         username = f"user{i}"
#         email = f"user{i}@example.com"
#         password = "password123"
#         cursor.execute(
#             sql.SQL("INSERT INTO Users (Username, Email, Password) VALUES (%s, %s, %s)"),
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
    # user_id = random.randint(1, 10001)  # Losowy identyfikator użytkownika
    user_id = 1
    date = datetime.now() - timedelta(days=random.randint(0, 365))  # Losowa data w ciągu ostatniego roku
    duration = random.randint(30, 120)  # Losowy czas trwania treningu w minutach
    cursor.execute(
        sql.SQL("INSERT INTO Sessions (User_ID, Date, Duration) VALUES (%s, %s, %s)"),
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
