cmake_minimum_required(VERSION 3.10)
project(NanoDB VERSION 0.2.0)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)

include_directories(include)

# 1. Find OpenSSL for SHA-256
find_package(OpenSSL REQUIRED)

# 2. Add Pybind11
add_subdirectory(third_party/pybind11)

# 3. Create the C++ Library
# Note: We now include src/nanodb.cpp
add_library(nanodb_lib src/nanodb.cpp)
target_link_libraries(nanodb_lib PRIVATE OpenSSL::Crypto)

# 4. Create the Python Module
pybind11_add_module(nanodb src/python_bridge.cpp)
target_link_libraries(nanodb PRIVATE nanodb_lib OpenSSL::Crypto)

# 5. Build the test runner
add_executable(nanodb_run tests/main.cpp)
target_link_libraries(nanodb_run nanodb_lib OpenSSL::Crypto)
