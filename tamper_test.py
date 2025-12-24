import sys
import os

sys.path.append(os.path.abspath("build"))
import nanodb

db = nanodb.Engine()

print("--- Integrity Audit ---")
if db.verify_chain():
    print("Initial State: VALID")
else:
    print("Initial State: CORRUPT")

# MANUALLY TAMPER WITH THE LEDGER FILE
print("\n[Hacker Action] Modifying ledger.db manually...")
with open("ledger.db", "r") as f:
    lines = f.readlines()

# Change 'Solar' to 'Coal' in the Renewables block
if len(lines) > 2:
    lines[2] = lines[2].replace("Solar", "Coal")

with open("ledger.db", "w") as f:
    f.writelines(lines)

print("[Audit] Re-verifying chain after manual edit...")
if db.verify_chain():
    print("Result: VALID (Audit Failed - Security Breach!)")
else:
    print("Result: CORRUPT (Audit Success - Tamper Detected!)")
