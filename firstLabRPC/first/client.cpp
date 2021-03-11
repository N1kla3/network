//
// Created by kolya on 3/7/21.
//

#include "functions.h"
#include "RPCLibrary/rpc.generated.h"

int main()
{
	InitLog();
	InitRPC();

	ManagerInfo info;
	info.name = "kolya";
	NetworkManager manager(MANAGER_TYPE::CLIENT);
	manager.SetManagerInfo(std::move(info));
	for (int i = 0; i < 11; i++)
    {
        manager.Connect("0.0.0.0", 22222);
		if (manager.IsConnected()) break;
		LOG_INFO("5 sec connect");
		sleep(1);
	}
	for (int i = 0; i < 12; i++)
    {
		manager.Tick(1);
		sleep(1);
	}
	manager.Client_Disconnect();
	return 0;
}