import pymongo
from pymongo import MongoClient
import random
from datetime import datetime, timedelta
import time

client = MongoClient('mongodb://localhost:27017')
db = client['test']

users_collection = db['Users']

def generate_users(end_range):
    time_start = time.time()
    bulk_operations = []
    for i in range(end_range):
        user = {
            'Username': f'user{i}',
            'Email': f'user{i}@example.com',
            'Password': 'password123' 
        }
        bulk_operations.append(user)
    users_collection.insert_many(bulk_operations)
    time_end = time.time()
    print("Time for ", end_range, " ", time_end-time_start)

generate_users(10)
generate_users(100)
generate_users(1000)
generate_users(10000)
generate_users(100000)

# sessions_collection = db['Sessions']

# # Funkcja do generowania daty w ciągu ostatnich 7 dni
# def generate_date():
#     return datetime.utcnow() - timedelta(days=random.randint(0, 6))

# # #Funkcja do generowania użytkowników

# # Funkcja do generowania sesji treningowych
# def generate_sessions():
#     for i in range(1, 11):
#         user_id = 1
#         # user_id = random.randint(1, 1000)  # Losowy identyfikator użytkownika
#         date = datetime.now() - timedelta(days=random.randint(0, 365))  # Losowa data w ciągu ostatniego roku
#         duration = random.randint(30, 120)  # Losowy czas trwania treningu w minutach
#         session = {
#             'User_ID': user_id,
#             'Date': date,
#             'Duration': duration
#         }
#         sessions_collection.insert_one(session)

#         # Wyświetlenie komunikatu co 10000 sesji
#         if i % 10000 == 0:
#             print(f'Inserted {i} sessions')

# # Generowanie użytkowników

# # Generowanie sesji treningowych
# generate_sessions()

# Zamknięcie połączenia
client.close()
