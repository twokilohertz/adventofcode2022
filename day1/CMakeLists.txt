cmake_minimum_required(VERSION 3.25)

project(day1
        VERSION 1.0
        DESCRIPTION "AOC 2022 Day 1"
        LANGUAGES CXX)

add_executable(day1 day1.cpp)

set_target_properties(day1 PROPERTIES
                        CXX_STANDARD 20
                        CXX_STANDARD_REQUIRED YES
                        CXX_EXTENSIONS NO)