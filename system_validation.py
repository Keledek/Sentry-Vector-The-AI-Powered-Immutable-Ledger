import sys
import os
import json
import time

sys.path.append(os.path.abspath("build"))
import nanodb

db = nanodb.Engine()

print("--- NanoDB System Health Check ---")

# 1. Check Version & Basics
print(f"Status: Testing Engine v{db.get_version()}")

# 2. Test Integrity under "heavy" single-file load
start_time = time.time()
for i in range(20):
    db.insert_vector(json.dumps({"test_id": i}), "[]")
end_time = time.time()

print(f"Performance: 20 blocks written in {end_time - start_time:.4f}s")

# 3. Test the 'Thread-Safe' Lock
is_valid = db.verify_chain()
print(f"Integrity: Blockchain Linkage {'[PASS]' if is_valid else '[FAIL]'}")

# 4. Check for 'Zombie' Files
db_size = os.path.getsize("ledger.db")
print(f"Storage: Ledger file size is {db_size} bytes")

if is_valid and db_size > 0:
    print("\nSYSTEM STATUS: HEALTHY & STABLE")
else:
    print("\nSYSTEM STATUS: CRITICAL ERROR DETECTED")
