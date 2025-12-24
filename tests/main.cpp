#include <iostream>
#include <vector>
#include "nanodb.hpp"

int main() {
    nanodb::NanoEngine db;
    
    std::cout << "--- NanoDB Vector Engine Test ---" << std::endl;
    
    // Test Vector Insertion (using an empty vector for basic test)
    std::string data = "{\"event\": \"system_test\", \"status\": \"ok\"}";
    std::string empty_vec = "[]"; 
    
    bool success = db.insert_vector(data, empty_vec);
    
    if (success) {
        std::cout << "Vector Insertion: SUCCESS" << std::endl;
    }

    // Test the new C++ Semantic Search logic
    std::vector<float> dummy_query = {0.1, 0.2, 0.3};
    auto results = db.semantic_search(dummy_query, 1);
    
    if (!results.empty()) {
        std::cout << "Search Logic: OPERATIONAL" << std::endl;
        std::cout << "Top Result Data: " << results[0].data << std::endl;
    }

    // Verify chain
    if (db.verify_chain()) {
        std::cout << "Ledger Integrity: VALID" << std::endl;
    }

    return 0;
}
