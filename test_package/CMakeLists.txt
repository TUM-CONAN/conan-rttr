cmake_minimum_required(VERSION 3.15)
cmake_policy(SET CMP0074 NEW)

project(test_package CXX)
set(CMAKE_VERBOSE_MAKEFILE TRUE)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(rttr REQUIRED CONFIG)
add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} rttr::rttr)