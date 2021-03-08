//
// Created by nicola on 10/02/2021.
//
#include "functions.h"
#include "RPCLibrary/rpc.generated.h"

int main()
{
	InitLog();
	InitRPC();
	NetworkManager manager(MANAGER_TYPE::SERVER, 22222);

	for (int i = 0; i < 300; i++)
    {
		manager.Tick(1);
		sleep(1);
	}
	manager.Server_Shutdown();
    return 0;
}