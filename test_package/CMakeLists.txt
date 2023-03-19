cmake_minimum_required(VERSION 3.1)
#set(CMAKE_C_COMPILER "gcc-10")
#set(CMAKE_CXX_COMPILER "g++-10")
project(PackageTest CXX)

find_package(secp256k1 CONFIG REQUIRED)

include_directories(../include)
add_executable(conan_integration_test conan_integration_test.cpp)
target_link_libraries(conan_integration_test secp256k1::secp256k1)


#target_compile_features(conan_integration_test PUBLIC cxx_std_20)
