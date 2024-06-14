import psycopg2
import random

conn = psycopg2.connect(
    dbname="gyms",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor.execute("SELECT id FROM sessions")
sessions = cursor.fetchall()
cursor.execute("SELECT id FROM exercises")
exercises = cursor.fetchall()

def add_session_exercise(session_id, exercise_id):
    sets = random.randint(3, 5)
    reps = random.randint(8, 12)
    weight = random.randint(20, 100)
    cursor.execute(
        "INSERT INTO session_exercise (session_id, exercise_id, sets, reps, weight) VALUES (%s, %s, %s, %s, %s)",
        (session_id, exercise_id, sets, reps, weight)
    )

for session in sessions:
    for exercise in exercises:
        add_session_exercise(session[0], exercise[0])

conn.commit()
cursor.close()
conn.close()