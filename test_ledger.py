import sys
import os
import json

# Add the build directory to the path so Python can find the .so module
sys.path.append(os.path.abspath("build"))

try:
    import nanodb
    print("--- NanoDB: Immutable Ledger Test ---")
    
    # Initialize the Ledger Engine
    db = nanodb.Engine()
    print(f"Engine Version: {db.get_version()}")

    # 1. Insert a professional log entry
    log_entry = {"event": "USER_LOGIN", "user_id": 1024, "status": "SUCCESS"}
    print("\nInserting Block 1...")
    db.insert("LOG_001", json.dumps(log_entry))

    # 2. Insert another entry to see the chain grow
    audit_entry = {"event": "DB_BACKUP", "status": "COMPLETED"}
    print("Inserting Block 2...")
    db.insert("LOG_002", json.dumps(audit_entry))

    # 3. Verify the Ledger
    print("\n--- Integrity Audit ---")
    print(f"Last Block Hash: {db.get_last_hash()}")
    print(f"Chain Verification: {'VALID' if db.verify_chain() else 'CORRUPTED'}")

    # 4. Check the physical file
    print("\n--- Ledger File Preview (ledger.db) ---")
    if os.path.exists("ledger.db"):
        with open("ledger.db", "r") as f:
            print(f.read())

except Exception as e:
    print(f"An error occurred: {e}")
