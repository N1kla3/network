set(CMAKE_CXX_STANDARD 20)
project(second)
ADD_DEFINITIONS(-DBOOST_LOG_DYN_LINK)
find_package(Boost REQUIRED COMPONENTS log log_setup REQUIRED)

include_directories(${Boost_INCLUDE_DIR})

add_library(liba ../RPClibrary/RPC.h ../RPClibrary/RPC.cpp ../RPClibrary/Stream.cpp ../RPClibrary/Stream.h ../RPClibrary/RPCManager.cpp ../RPClibrary/RPCManager.h ../RPClibrary/Socket.cpp ../RPClibrary/Socket.h ../RPClibrary/SocketFactory.cpp ../RPClibrary/SocketFactory.h)
add_executable(second main.cpp)

target_link_libraries(liba Boost::log Boost::log_setup)
target_link_libraries(second liba)