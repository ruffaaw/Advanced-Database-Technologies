CREATE DATABASE gyms;

\c gyms

CREATE TABLE IF NOT EXISTS Users (
    ID SERIAL PRIMARY KEY,
    Username VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS Exercises (
    ID SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS Workouts (
    ID SERIAL PRIMARY KEY,
    User_ID INT NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES Users(ID)
);

CREATE TABLE IF NOT EXISTS Workout_Exercise (
    ID SERIAL PRIMARY KEY,
    Workout_ID INT NOT NULL,
    Exercise_ID INT NOT NULL,
    Sets INT,
    Reps INT,
    Weight FLOAT,
    FOREIGN KEY (Workout_ID) REFERENCES Workouts(ID),
    FOREIGN KEY (Exercise_ID) REFERENCES Exercises(ID)
);

CREATE TABLE IF NOT EXISTS Sessions (
    ID SERIAL PRIMARY KEY,
    User_ID INT NOT NULL,
    Date DATE NOT NULL,
    Duration INT,
    FOREIGN KEY (User_ID) REFERENCES Users(ID)
);

CREATE TABLE IF NOT EXISTS Session_Exercise (
    ID SERIAL PRIMARY KEY,
    Session_ID INT NOT NULL,
    Exercise_ID INT NOT NULL,
    Sets INT,
    Reps INT,
    Weight FLOAT,
    FOREIGN KEY (Session_ID) REFERENCES Sessions(ID),
    FOREIGN KEY (Exercise_ID) REFERENCES Exercises(ID)
);