# 🛡️ Sentry-Vector: Secure AI-Ledger Engine
**Author:** Sounak Chatterjee  
**Version:** 1.2.0 (Stable)



## 🌟 Overview
Sentry-Vector is an industrial-grade, embedded NoSQL database designed for the modern AI era. It bridges the gap between **Semantic Intelligence** and **Cryptographic Security**. Unlike traditional databases, Sentry-Vector stores data in an immutable blockchain-style ledger while providing lightning-fast AI-powered search capabilities.

## 🚀 Key Architectural Features

### 1. AI-Driven Semantic Search
Most databases search for exact words. Sentry-Vector searches for **intent**. Using the `all-MiniLM-L6-v2` transformer model, it converts text into 384-dimensional vectors. The C++ core then performs high-speed **Cosine Similarity** math to find conceptually related data.

### 2. Immutable Blockchain Ledger
Every entry (block) is cryptographically linked to the previous one. 
- **HMAC-SHA256 Security:** Each block hash is calculated using a "Secret Pepper," making it impossible for unauthorized users to forge history.
- **Auditability:** The system includes a `verify_chain()` function that performs a full cryptographic audit of the database integrity.

### 3. High-Performance C++ Core
- **In-Memory Indexing:** Vectors are cached in RAM upon startup for (1)$ to (\log n)$ search performance.
- **Thread-Safety:** Implements `std::mutex` locks to ensure data consistency during concurrent AI operations.
- **Python Bindings:** Seamlessly integrated with Python via `Pybind11`.

---

## 🏗️ Technical Specification
- **Language:** C++17, Python 3.10+
- **Cryptography:** OpenSSL SHA256
- **Mathematics:** Vector Space Modeling (Cosine Similarity)
- **Build System:** CMake 3.10+

---

## 🛠️ Installation & Usage

### 1. Build the Engine
```bash
mkdir build && cd build
cmake ..
make
```

### 2. Run AI Search Demo
```bash
python3 active_ai_search.py
```

### 3. Run Security Audit
```bash
python3 tamper_test.py
```

## 🗺️ Roadmap
- **v1.3:** AES-256 Encryption for data-at-rest.
- **v1.4:** Persistent B-Tree indexing for billion-scale datasets.
- **v1.5:** Distributed consensus (p2p) for multi-node ledgers.

---
**GOAT Status:** Developed with the precision of a MESSI free-kick. ⚽
