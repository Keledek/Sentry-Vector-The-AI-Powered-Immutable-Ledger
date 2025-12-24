import sys
import os
import json
sys.path.append(os.path.abspath("build"))
import nanodb

db = nanodb.Engine()

# Insert a complex JSON document
user_data = {
    "name": "Messi",
    "club": "Inter Miami",
    "stats": {"goals": 800, "assists": 350},
    "is_goat": True
}

db.insert("player_10", json.dumps(user_data))

# Retrieve and parse back in Python
raw_data = db.find_one("player_10")
data = json.loads(raw_data)

print(f"--- Database Result ---")
print(f"Name: {data['name']}")
print(f"Goals: {data['stats']['goals']}")
print(f"GOAT Status: {'Confirmed' if data['is_goat'] else 'N/A'}")
