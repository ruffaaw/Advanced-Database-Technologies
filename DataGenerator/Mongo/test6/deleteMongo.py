from pymongo import MongoClient
import time

client = MongoClient('localhost', 27017)
db = client['test']
sessions_collection = db['Sessions']

def delete_sessions_in_batches(batch_size):
    start_time = time.time()

    session_ids = sessions_collection.find(
        {},
        {"_id": 1}
    ).limit(batch_size)
    
    session_ids = [session["_id"] for session in session_ids]
    
    sessions_collection.delete_many({"_id": {"$in": session_ids}})
    
    end_time = time.time()
    print(f"Time for deleting {batch_size} sessions: ", end_time - start_time, " s")

delete_sessions_in_batches(10)
delete_sessions_in_batches(100)
delete_sessions_in_batches(1000)
delete_sessions_in_batches(10000)
delete_sessions_in_batches(100000)

client.close()
