cmake_minimum_required(VERSION 3.3)
project(mownit_lab1)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    gauss.cpp)

add_executable(mownit_lab1 ${SOURCE_FILES})