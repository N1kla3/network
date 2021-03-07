//
// Created by kolya on 3/7/21.
//

#include "functions.h"
#include "RPCLibrary/rpc.generated.h"

int main()
{
	InitLog();
	InitRPC();

	NetworkManager manager(MANAGER_TYPE::CLIENT);
	manager.Connect("127.0.0.1", 22222);



	return 0;
}