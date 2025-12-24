#ifndef BLOCK_HPP
#define BLOCK_HPP

#include <string>
#include <vector>
#include <openssl/sha.h>
#include <iomanip>
#include <sstream>

class Block {
public:
    int index;
    std::string previous_hash;
    std::string hash;
    std::string data;
    std::string secret_pepper = "GOAT_MESSI_10_SECURITY"; // Our secret key

    Block(int idx, const std::string& prev_hash, const std::string& data_content)
        : index(idx), previous_hash(prev_hash), data(data_content) {
        hash = calculate_sha256();
    }

    std::string calculate_sha256() const {
        std::stringstream ss;
        // We mix the secret pepper into the hash input
        ss << index << previous_hash << data << secret_pepper;
        std::string input = ss.str();

        unsigned char hash_result[SHA256_DIGEST_LENGTH];
        SHA256_CTX sha256;
        SHA256_Init(&sha256);
        SHA256_Update(&sha256, input.c_str(), input.size());
        SHA256_Final(hash_result, &sha256);

        std::stringstream hash_str;
        for(int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
            hash_str << std::hex << std::setw(2) << std::setfill('0') << (int)hash_result[i];
        }
        return hash_str.str();
    }
};

#endif
