cmake_minimum_required(VERSION 3.17)
set(CMAKE_CXX_STANDARD 20)
project(first)

add_subdirectory(RPCLibrary)

message(${PROJECT_SOURCE_DIR})
HeaderTool(functions.h)
#add_custom_command(OUTPUT /home/kolya/CLionProjects/network/firstLabRPC/first/RPCLibrary/rpc.generated.h /home/kolya/CLionProjects/network/firstLabRPC/first/RPCLibrary/rpc.generated.cpp
#       COMMAND RPCHeaderTool ${PROJECT_SOURCE_DIR} ${PROJECT_SOURCE_DIR}/RPCLibrary
#       DEPENDS functions.h RPCHeaderTool
#       COMMENT "generating files"
#       )

add_executable(first main.cpp functions.h ${PROJECT_SOURCE_DIR}/RPCLibrary/rpc.generated.h ${PROJECT_SOURCE_DIR}/RPCLibrary/rpc.generated.cpp functions.cpp)

target_link_libraries(first RPClibrary )