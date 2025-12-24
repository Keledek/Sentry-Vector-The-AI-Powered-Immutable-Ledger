import sys
import os
import threading
import json
import time

sys.path.append(os.path.abspath("build"))
import nanodb

db = nanodb.Engine()

def hammer_db(thread_id):
    for i in range(10):
        data = {"thread": thread_id, "loop": i, "msg": "Concurrent write test"}
        db.insert_vector(json.dumps(data), "[]")
        print(f"Thread {thread_id} wrote block {i}")

threads = []
print("Starting Concurrent Hammer Test...")
for i in range(5):
    t = threading.Thread(target=hammer_db, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nAll threads finished. Running Integrity Audit...")
if db.verify_chain():
    print("RESULT: Chain is STABLE and VALID.")
else:
    print("RESULT: Chain is CORRUPTED (Concurrency Failure).")
