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
batch_size = 1000
while True:
    start_time = time.time()
    cursor.execute("""
        DELETE FROM sessions 
        WHERE id IN (
            SELECT id 
            FROM sessions 
            WHERE date < NOW() - INTERVAL '6 months'
            LIMIT %s
        )
        RETURNING id;
    """, (batch_size,))
    deleted_rows = cursor.fetchall()
    conn.commit()
    if len(deleted_rows) < batch_size:
        break

end_time = time.time()
print("Delete time: ", end_time - start_time, " s")
cursor.close()
conn.close()
