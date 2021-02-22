set(CMAKE_CXX_STANDARD 20)
project(first)

add_executable(first main.cpp)
add_library(lib ../RPClibrary/RPC.h ../RPClibrary/RPC.cpp ../RPClibrary/RPCManager.cpp ../RPClibrary/RPCManager.h ../RPClibrary/Socket.cpp ../RPClibrary/Socket.h ../RPClibrary/SocketFactory.cpp ../RPClibrary/SocketFactory.h ../RPClibrary/TCPSocket.cpp ../RPClibrary/TCPSocket.h ../RPClibrary/SocketUtil.cpp ../RPClibrary/SocketUtil.h ../RPClibrary/NetworkManager.cpp ../RPClibrary/NetworkManager.h)

target_link_libraries(first lib)