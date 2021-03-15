//
// Created by nicola on 10/02/2021.
//
#include "functions.h"
#include "RPCLibrary/rpc.generated.h"

int main()
{
	InitLog();
	InitRPC();
	auto manager = std::make_unique<NetworkManager>(MANAGER_TYPE::SERVER, 22222);
	std::vector<int> vec{3, 4, 5, 6, 6};

	for (int i = 0; i < 300; i++)
    {
		manager->Tick(1);
		write_function(*manager, 3, 4);
		write_third(*manager, 1.f, vec);
		sleep(1);
	}
	manager->Server_Shutdown();
    return 0;
}