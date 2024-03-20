import sqlite3

conn = sqlite3.connect('./gym.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Exercises (
        ExerciseID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Description TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Workouts (
        WorkoutID INTEGER PRIMARY KEY,
        User_ID INTEGER NOT NULL,
        Date TEXT NOT NULL,
        FOREIGN KEY (User_ID) REFERENCES Users (UserID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Workout_Exercise (
        Workout_Exercise_ID INTEGER PRIMARY KEY,
        Workout_ID INTEGER NOT NULL,
        Exercise_ID INTEGER NOT NULL,
        Sets INTEGER NOT NULL,
        Reps INTEGER NOT NULL,
        Weight REAL NOT NULL,
        FOREIGN KEY (Workout_ID) REFERENCES Workouts (WorkoutID),
        FOREIGN KEY (Exercise_ID) REFERENCES Exercises (ExerciseID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sessions (
        SessionID INTEGER PRIMARY KEY,
        User_ID INTEGER NOT NULL,
        Date TEXT NOT NULL,
        Duration INTEGER NOT NULL,
        FOREIGN KEY (User_ID) REFERENCES Users (UserID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Session_Exercise (
        Session_Exercise_ID INTEGER PRIMARY KEY,
        Session_ID INTEGER NOT NULL,
        Exercise_ID INTEGER NOT NULL,
        Sets INTEGER NOT NULL,
        Reps INTEGER NOT NULL,
        Weight REAL NOT NULL,
        FOREIGN KEY (Session_ID) REFERENCES Sessions (SessionID),
        FOREIGN KEY (Exercise_ID) REFERENCES Exercises (ExerciseID)
    )
''')

conn.commit()
conn.close()