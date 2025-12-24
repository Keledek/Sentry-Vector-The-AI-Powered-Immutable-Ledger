import sys
import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Point to the build directory where nanodb.so is located
sys.path.append(os.path.abspath("build"))
import nanodb

# 2. Load the AI Model
print("--- Initializing AI Intelligence (MiniLM) ---")
model = SentenceTransformer('all-MiniLM-L6-v2')

# 3. Initialize the Engine
db = nanodb.Engine()
print(f"Engine Version: {db.get_version()}")

# 4. Professional Financial Intelligence Data
market_intelligence = [
    {"topic": "Quantum Finance", "msg": "Major banks are pivoting to post-quantum encryption to protect digital assets."},
    {"topic": "Renewables", "msg": "Solar panel efficiency has reached a new record, driving down renewable energy costs and electricity prices."},
    {"topic": "Regulatory", "msg": "New regulations in the EU aim to track large Bitcoin transactions for tax compliance."},
    {"topic": "Semiconductors", "msg": "Supply chain constraints in high-end lithography are slowing down 2nm chip production."}
]

# Wipe old ledger to ensure fresh format
if os.path.exists("ledger.db"):
    os.remove("ledger.db")
    db = nanodb.Engine()

# 5. Insert data with AI Embeddings
print("\n[Action] Securing Intelligence into Immutable Ledger...")
for item in market_intelligence:
    # Generate vector in Python
    vec = model.encode(item['msg']).tolist()
    # Store in C++ Engine
    db.insert_vector(json.dumps(item), json.dumps(vec))

# 6. PERFORM THE C++ SEARCH
# We search for "green energy" - it should match "Renewables"
query = "Tell me about green energy and electricity prices."
print(f"\n[Search] Querying: '{query}'")

query_vec = model.encode(query).tolist()

# This calls the C++ logic we just wrote!
results = db.semantic_search(query_vec, 1)

if results:
    best = results[0]
    print("\n" + "="*30)
    print("--- C++ SEMANTIC MATCH ---")
    print(f"Similarity Score: {best.score:.4f}")
    print(f"Recovered Data:   {best.data}")
    print("="*30)
else:
    print("No matches found.")
