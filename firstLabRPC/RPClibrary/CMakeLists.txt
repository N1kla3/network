cmake_minimum_required(VERSION 3.17)
project(RPClibrary)
set(CMAKE_CXX_STANDARD 20)

SET(Boost_USE_STATIC_LIBS ON)
find_package(Boost REQUIRED COMPONENTS log REQUIRED)

include_directories(${Boost_INCLUDE_DIR})


add_library(RPClibrary  RPC.cpp Stream.cpp Stream.h RPCManager.cpp RPCManager.h Socket.cpp Socket.h SocketFactory.cpp SocketFactory.h TCPSocket.cpp TCPSocket.h SocketUtil.cpp SocketUtil.h NetworkManager.cpp NetworkManager.h)
target_precompile_headers(RPClibrary PUBLIC RPC.h)

target_link_libraries(RPClibrary Boost::log)