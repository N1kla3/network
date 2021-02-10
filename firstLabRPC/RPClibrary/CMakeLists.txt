cmake_minimum_required(VERSION 3.17)
project(RPClibrary)
set(CMAKE_CXX_STANDARD 20)

add_library(RPClibrary RPC.h RPC.cpp)