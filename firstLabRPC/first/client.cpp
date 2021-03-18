//
// Created by kolya on 3/7/21.
//

#include "RPCLibrary/rpc.generated.h"
#include "functions.h"

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
	manager.SetManagerInfo(std::move(info));
	for (int i = 0; i < 11; i++)
    {
        manager.Connect("0.0.0.0:22222");
		if (manager.IsConnected()) break;
		sleep(1);
	}
	for (int i = 0; i < 30; i++)
    {
		manager.Tick(1);
        write_increaseNumber(manager, i);
		sleep(1);
	}
	manager.Client_Disconnect();
	return 0;
}