#ifndef NANODB_HPP
#define NANODB_HPP

#include <string>
#include <vector>
#include <mutex>
#include "block.hpp"

namespace nanodb {

struct SearchResult {
    float score;
    std::string data;
};

// New internal struct for high-speed indexing
struct VectorIndex {
    std::vector<float> embedding;
    std::string data; // Cache the data string for instant retrieval
};

class NanoEngine {
public:
    NanoEngine();
    ~NanoEngine();

    bool insert_vector(const std::string& json_data, const std::string& vec_str);
    std::vector<SearchResult> semantic_search(const std::vector<float>& query_vec, int top_k);
    
    bool verify_chain() const;
    std::string getVersion() const;

private:
    std::string db_file = "ledger.db";
    std::string last_hash;
    size_t current_index;
    
    mutable std::mutex db_mutex;
    
    // THE INDEX: High-speed RAM storage
    std::vector<VectorIndex> memory_index;

    void load_ledger(); 
    void create_genesis_block();
};

} // namespace nanodb

#endif
