//
// Created by kolya on 3/19/21.
//
#include "RPCLibrary/RPC.h"
#include "RPCLibrary/rpc.generated.h"

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		return -1;
	}

	InitLog();
	InitRPC();

	ManagerInfo info;
	info.name = argv[1];
	NetworkManager manager(MANAGER_TYPE::CLIENT);
	manager.SetConnectionTimeLimit(10);
	manager.SetManagerInfo(std::move(info));
	for (int i = 0; i < 3; i++)
    {
        manager.Connect("0.0.0.0:22222");
		if (manager.IsConnected()) break;
		else sleep(1);
	}
	for (int i = 0; i < 30; i++)
	{
		manager.Tick(1);
		write_addToVector(manager, {1,1,1});
		write_setRotation(manager, {1,2,2});
		sleep(1);
	}
	manager.Client_Disconnect();
	return 0;
}