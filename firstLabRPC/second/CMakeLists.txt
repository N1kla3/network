set(CMAKE_CXX_STANDARD 20)
project(second)

add_executable(second main.cpp)
add_library(liba ../RPClibrary/RPC.cpp ../RPClibrary/RPC.h)

target_link_libraries(second liba)