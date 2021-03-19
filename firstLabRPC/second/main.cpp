//
// Created by nicola on 10/02/2021.
//
#include "RPCLibrary/RPC.h"
#include "RPCLibrary/rpc.generated.h"

int main()
{
    InitLog();
	InitRPC();
    NetworkManager manager(MANAGER_TYPE::SERVER);
	for (int i = 0; i < 1111; i++)
    {
		manager.Tick(1);
		write_printVectors(manager);
		sleep(1);
	}
	manager.Server_Shutdown();
    return 0;
}
