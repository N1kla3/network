set(CMAKE_CXX_STANDARD 20)
project(first)

add_executable(first main.cpp)
add_library(lib ../RPClibrary/RPC.h ../RPClibrary/RPC.cpp)

target_link_libraries(first lib)