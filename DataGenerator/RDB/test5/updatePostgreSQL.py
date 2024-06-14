import psycopg2
import time

conn = psycopg2.connect(
    dbname="gyms",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
start_time=time.time()
for user_id in range(1, 11):
    new_password = f"password10"
    cursor.execute("UPDATE Users SET Password = %s WHERE ID = %s", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 10: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 101):
    new_password = f"password100"
    cursor.execute("UPDATE Users SET Password = %s WHERE ID = %s", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 100: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 1001):
    new_password = f"password1000"
    cursor.execute("UPDATE Users SET Password = %s WHERE ID = %s", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 1000: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 10001):
    new_password = f"password10000"
    cursor.execute("UPDATE Users SET Password = %s WHERE ID = %s", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 10000: ", end_time-start_time, " s")

start_time=time.time()
for user_id in range(1, 100001):
    new_password = f"password100000"
    cursor.execute("UPDATE Users SET Password = %s WHERE ID = %s", (new_password, user_id))
conn.commit()
end_time=time.time()
print("Time for 100000: ", end_time-start_time, " s")

cursor.close()
conn.close()