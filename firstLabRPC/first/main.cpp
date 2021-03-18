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
	manager->SetConnectionTimeLimit(3);
	manager->SetNetFrequency(0.33f);
	manager->SetSecurityLevel(SECURITY_LEVEL::COMMON);

	for (int i = 0; i < 300; i++)
    {
		manager->Tick(1);
		if (updated)
        {
			write_answer(*manager);
			answer();
		}
		sleep(1);
	}
	manager->Server_Shutdown();
    return 0;
}