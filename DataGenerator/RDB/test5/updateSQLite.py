import sqlite3
import time

conn = sqlite3.connect('C:\Studia\Magisterka\Semestr1\ZTBD\SQLite\gym.db')
cursor = conn.cursor()

start_time=time.time()
for user_id in range(1, 11):
    new_password = f"new_password_{user_id}"
    cursor.execute("UPDATE Users SET Password = ? WHERE ID = ?", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 10: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 101):
    new_password = f"new_password_{user_id}"
    cursor.execute("UPDATE Users SET Password = ? WHERE ID = ?", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 100: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 1001):
    new_password = f"new_password_{user_id}"
    cursor.execute("UPDATE Users SET Password = ? WHERE ID = ?", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 1000: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 10001):
    new_password = f"new_password_{user_id}"
    cursor.execute("UPDATE Users SET Password = ? WHERE ID = ?", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 10000: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 100001):
    new_password = f"new_password_{user_id}"
    cursor.execute("UPDATE Users SET Password = ? WHERE ID = ?", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 100000: ", end_time-start_time, " s")

cursor.close()
conn.close()
