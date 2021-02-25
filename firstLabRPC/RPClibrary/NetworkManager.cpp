//
// Created by nicola on 22/02/2021.
//

#include "RPC.h"
#include "RPCManager.h"

#include "NetworkManager.h"
#include "Socket.h"


NetworkManager::NetworkManager(MANAGER_TYPE type, int port)
		:
		m_Type(type),
		m_Port(port)
{

	m_Socket = SocketUtil::CreateTCPSocket(INET);
	SocketAddress addr(INADDR_ANY, port);
	m_Socket->Bind(addr);

	if (type == MANAGER_TYPE::SERVER)
	{
		LOG_INFO(Server at port) << port;
	}
	else if (type == MANAGER_TYPE::CLIENT)
	{
		LOG_INFO(Client init at port ) << port;
	}
}

NetworkManager::~NetworkManager()
= default;

void NetworkManager::CreatePacket()
{
}

void NetworkManager::SendPacket()
{
}

void NetworkManager::ReceivePacket()
{
}

void NetworkManager::SetNetFrequency(float frequency)
{
}

void NetworkManager::HaveReceivedData() const noexcept
{
}

void NetworkManager::SetManagerMode(MANAGER_MODE mode) const
{
}

MANAGER_MODE NetworkManager::GetManagerMode() const
{

	return MANAGER_MODE::FREQUENCY;
}

void NetworkManager::Connect(const std::string& address)
{
}

void NetworkManager::Tick(float deltaTime)
{
}

MANAGER_TYPE NetworkManager::GetManagerType() const noexcept
{

	return m_Type;
}
