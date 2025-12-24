#define JSON_ASSERT(x) 
#include "nanodb.hpp"
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

namespace nanodb {

NanoEngine::NanoEngine() : current_index(0), last_hash("0") {
    load_ledger();
    if (current_index == 0) create_genesis_block();
}

NanoEngine::~NanoEngine() {}

void NanoEngine::create_genesis_block() {
    std::lock_guard<std::mutex> lock(db_mutex);
    Block genesis(0, "0", "{\"note\": \"Genesis Block\"}");
    last_hash = genesis.hash;
    current_index = 1;
    std::ofstream outfile(db_file, std::ios::binary | std::ios::app);
    outfile << genesis.index << "|" << genesis.previous_hash << "|" << genesis.hash << "|[]|" << genesis.data << "\n";
    outfile.close();
}

bool NanoEngine::insert_vector(const std::string& json_data, const std::string& vec_str) {
    std::lock_guard<std::mutex> lock(db_mutex);
    Block new_block(current_index, last_hash, json_data);
    
    std::ofstream outfile(db_file, std::ios::binary | std::ios::app);
    if (!outfile.is_open()) return false;
    outfile << new_block.index << "|" << new_block.previous_hash << "|" << new_block.hash << "|" << vec_str << "|" << new_block.data << "\n";
    outfile.close();

    try {
        json j_vec = json::parse(vec_str);
        if (!j_vec.empty()) {
            memory_index.push_back({j_vec.get<std::vector<float>>(), json_data});
        }
    } catch(...) {}

    last_hash = new_block.hash;
    current_index++;
    return true;
}

std::vector<SearchResult> NanoEngine::semantic_search(const std::vector<float>& query_vec, int top_k) {
    std::lock_guard<std::mutex> lock(db_mutex);
    std::vector<SearchResult> all_results;
    for (const auto& item : memory_index) {
        float dot = 0.0, d1 = 0.0, d2 = 0.0;
        for(size_t i = 0; i < query_vec.size(); ++i) {
            dot += query_vec[i] * item.embedding[i];
            d1 += query_vec[i] * query_vec[i];
            d2 += item.embedding[i] * item.embedding[i];
        }
        float score = (d1 > 0 && d2 > 0) ? dot / (std::sqrt(d1) * std::sqrt(d2)) : 0;
        all_results.push_back({score, item.data});
    }
    std::sort(all_results.begin(), all_results.end(), [](const SearchResult& a, const SearchResult& b) {
        return a.score > b.score;
    });
    if (all_results.size() > (size_t)top_k) all_results.resize(top_k);
    return all_results;
}

bool NanoEngine::verify_chain() const {
    std::lock_guard<std::mutex> lock(db_mutex);
    std::ifstream infile(db_file);
    std::string line, expected_prev = "0";
    
    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        std::vector<std::string> p;
        std::string pt;
        while (std::getline(ss, pt, '|')) p.push_back(pt);
        if (p.size() < 5) continue;

        // 1. Linkage Check
        if (p[1] != expected_prev) return false;

        // 2. SECRET KEY AUDIT: Re-calculate hash with our secret pepper
        Block temp_block(std::stoi(p[0]), p[1], p[4]);
        if (temp_block.hash != p[2]) {
            std::cout << "CRITICAL: Hash mismatch at block " << p[0] << ". Tampering detected!" << std::endl;
            return false;
        }

        expected_prev = p[2];
    }
    return true;
}

void NanoEngine::load_ledger() {
    std::ifstream infile(db_file);
    if (!infile.is_open()) return;
    std::string line;
    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        std::vector<std::string> p;
        std::string pt;
        while (std::getline(ss, pt, '|')) p.push_back(pt);
        if(p.size() >= 5) {
            current_index = std::stoul(p[0]) + 1;
            last_hash = p[2];
            try {
                json j_vec = json::parse(p[3]);
                if (!j_vec.empty()) memory_index.push_back({j_vec.get<std::vector<float>>(), p[4]});
            } catch(...) {}
        }
    }
}

std::string NanoEngine::getVersion() const { return "1.2.0-secure-hmac"; }

} // namespace nanodb
