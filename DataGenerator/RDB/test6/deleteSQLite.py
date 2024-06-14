import sqlite3
import time

conn = sqlite3.connect('C:/Studia/Magisterka/Semestr1/ZTBD/SQLite/gym.db')

cursor = conn.cursor()
cursor.execute("SELECT id FROM session_exercise")
session_exercise = cursor.fetchall()
session_ids = [se[0] for se in session_exercise]

start_time = time.time()
for session_id in range(min(session_ids), min(session_ids)+11):
    cursor.execute("DELETE FROM session_exercise WHERE id = ?", (session_id,))
conn.commit()
end_time = time.time()
print("Time for 10: ", end_time-start_time, " s")

cursor.execute("SELECT id FROM session_exercise")
session_exercise = cursor.fetchall()
session_ids = [se[0] for se in session_exercise]
start_time = time.time()
for session_id in range(min(session_ids), min(session_ids)+101):
    cursor.execute("DELETE FROM session_exercise WHERE id = ?", (session_id,))
conn.commit()
end_time = time.time()
print("Time for 100: ", end_time-start_time, " s")

cursor.execute("SELECT id FROM session_exercise")
session_exercise = cursor.fetchall()
session_ids = [se[0] for se in session_exercise]
start_time = time.time()
for session_id in range(min(session_ids), min(session_ids)+1001):
    cursor.execute("DELETE FROM session_exercise WHERE id = ?", (session_id,))
conn.commit()
end_time = time.time()
print("Time for 1000: ", end_time-start_time, " s")

cursor.execute("SELECT id FROM session_exercise")
session_exercise = cursor.fetchall()
session_ids = [se[0] for se in session_exercise]
start_time = time.time()
for session_id in range(min(session_ids), min(session_ids)+10001):
    cursor.execute("DELETE FROM session_exercise WHERE id = ?", (session_id,))
conn.commit()
end_time = time.time()
print("Time for 10000: ", end_time-start_time, " s")

cursor.execute("SELECT id FROM session_exercise")
session_exercise = cursor.fetchall()
session_ids = [se[0] for se in session_exercise]
start_time = time.time()
for session_id in range(min(session_ids), min(session_ids)+100001):
    cursor.execute("DELETE FROM session_exercise WHERE id = ?", (session_id,))
conn.commit()
end_time = time.time()
print("Time for 100000: ", end_time-start_time, " s")

cursor.close()
conn.close()
