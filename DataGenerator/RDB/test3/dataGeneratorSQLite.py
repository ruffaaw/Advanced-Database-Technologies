import sqlite3
import random

conn = sqlite3.connect('C:/Studia/Magisterka/Semestr1/ZTBD/SQLite/gym.db')
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
        "INSERT INTO session_Exercise (session_id, exercise_id, sets, reps, weight) VALUES (?, ?, ?, ?, ?)",
        (session_id, exercise_id, sets, reps, weight)
    )

for session in sessions:
    for exercise in exercises:
        add_session_exercise(session[0], exercise[0])

conn.commit()
cursor.close()
conn.close()