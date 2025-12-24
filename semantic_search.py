import sys
import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Add build path for nanodb
sys.path.append(os.path.abspath("build"))
import nanodb

# 1. Load the AI Model (Small, fast, professional)
print("--- Loading AI Intelligence Model ---")
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Initialize NanoDB (Vector Edition)
db = nanodb.Engine()
print(f"NanoDB Version: {db.get_version()}")

# 3. Data Entry (Professional Financial Intelligence)
market_news = [
    {"topic": "Semiconductors", "info": "The demand for high-end GPUs is soaring due to the rapid growth of generative AI models."},
    {"topic": "Central Banks", "info": "The European Central Bank signals a potential rate cut as inflation begins to stabilize below 2%."},
    {"topic": "Cybersecurity", "info": "New zero-day vulnerabilities in cloud infrastructure have led to increased spending on enterprise security."}
]

# Wipe old ledger to ensure fresh vector format
if os.path.exists("ledger.db"):
    os.remove("ledger.db")
    db = nanodb.Engine()

# 4. Insert data with AI Embeddings
print("\nEncoding and Securing Market Data in Ledger...")
for item in market_news:
    content = item['info']
    # Generate the vector (embedding)
    vector = model.encode(content).tolist()
    # Save into the Immutable Ledger
    db.insert_vector(json.dumps(item), json.dumps(vector))

# 5. SEMANTIC SEARCH FUNCTION
def semantic_search(query_text):
    print(f"\nSearching for: '{query_text}'")
    query_vec = model.encode(query_text)
    
    results = []
    
    # Read the ledger file manually to perform vector math
    with open("ledger.db", "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) < 5: continue
            
            # parts[3] is our Vector, parts[4] is our JSON Data
            stored_vec = np.array(json.loads(parts[3]))
            if len(stored_vec) == 0: continue # Skip genesis
            
            # Calculate Cosine Similarity
            similarity = np.dot(query_vec, stored_vec) / (np.linalg.norm(query_vec) * np.linalg.norm(stored_vec))
            
            results.append((similarity, parts[4]))
    
    # Sort by similarity (highest first)
    results.sort(key=lambda x: x[0], reverse=True)
    return results[0] if results else (0, "No data found")

# 6. Test the AI
query = "Tell me about interest rates and inflation."
score, best_match = semantic_search(query)

print("\n--- AI TOP MATCH ---")
print(f"Confidence Score: {score:.4f}")
print(f"Result: {best_match}")
