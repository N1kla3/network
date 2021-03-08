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
	for (int i = 0; i < 5; i++)
    {
        manager.Connect("0.0.0.0", 22222);
		LOG_INFO(5 sec connect);
		sleep(1);
	}
	manager.Client_Disconnect();
	return 0;
}