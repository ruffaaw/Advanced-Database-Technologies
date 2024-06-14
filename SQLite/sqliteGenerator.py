import sqlite3

conn = sqlite3.connect('./gym.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS workouts (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS workout_exercise (
        id INTEGER PRIMARY KEY,
        workout_ID INTEGER NOT NULL,
        exercise_ID INTEGER NOT NULL,
        sets INTEGER NOT NULL,
        reps INTEGER NOT NULL,
        weight REAL NOT NULL,
        FOREIGN KEY (workout_id) REFERENCES workouts (id),
        FOREIGN KEY (exercise_id) REFERENCES exercises (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY,
        user_ID INTEGER NOT NULL,
        date TEXT NOT NULL,
        duration INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS session_Exercise (
        id INTEGER PRIMARY KEY,
        session_id INTEGER NOT NULL,
        exercise_id INTEGER NOT NULL,
        sets INTEGER NOT NULL,
        reps INTEGER NOT NULL,
        weight REAL NOT NULL,
        FOREIGN KEY (session_id) REFERENCES sessions (id),
        FOREIGN KEY (exercise_id) REFERENCES sxercises (id)
    )
''')

conn.commit()
conn.close()