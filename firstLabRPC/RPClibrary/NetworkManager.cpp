//
// Created by nicola on 22/02/2021.
//

#include "RPC.h"
#include "RPCManager.h"
#include "Stream.h"
#include "NetworkManager.h"
#include "SocketFactory.h"
#include <memory>
#include "Socket.h"


NetworkManager::NetworkManager(MANAGER_TYPE type, int port)
		:
		m_Type(type),
		m_Port(port)
{

	m_Socket = SocketUtil::CreateTCPSocket(INET);
	if (type == MANAGER_TYPE::SERVER)
	{
		SocketAddress addr(INADDR_ANY, port);
		m_Socket->Bind(addr);
		LOG_INFO(Server at port) << port;
	}
	else if (type == MANAGER_TYPE::CLIENT)
	{
		LOG_INFO(Client init);
	}
}

NetworkManager::~NetworkManager()
= default;

void NetworkManager::CreatePacket()
{

	m_OutStreamPtr = std::make_unique<OutputMemoryBitStream>();
}

void NetworkManager::SetNetFrequency(float frequency)
{
	m_NetFrequency = frequency;
}

void NetworkManager::HaveReceivedData() const noexcept
{
}

void NetworkManager::SetManagerMode(MANAGER_MODE mode)
{
	m_Mode = mode;
}

MANAGER_MODE NetworkManager::GetManagerMode() const
{
	return m_Mode;
}

/** Not accessible in server */
void NetworkManager::Connect(const std::string& address)
{
	if (m_Type == MANAGER_TYPE::CLIENT)
	{
		if (m_Socket->Connect(*SocketFactory::CreateIPv4FromString(address)) < 0)
		{
			LOG_ERROR(NetworkManager::Connect ) << address;
		}
		else bClientConnected = true;
	}
	else LOG_WARNING(Connect can only be used in client);
}

void NetworkManager::Tick(float deltaTime)
{
}

MANAGER_TYPE NetworkManager::GetManagerType() const noexcept
{
	return m_Type;
}

void NetworkManager::HandleHelloPacket()
{

	if (m_Type == MANAGER_TYPE::SERVER)
	{
		ManagerInfo info;
		info.Read(*m_InStreamPtr);

	}
}

void NetworkManager::HandleRejectedPacket()
{

}

void NetworkManager::HandleFunctionPacket()
{

}

void NetworkManager::SendHello()
{
	m_OutStreamPtr->WriteBits(PACKET::HELLO, GetRequiredBits<PACKET::MAX>::VALUE);
	if (m_Type == MANAGER_TYPE::CLIENT)
	{
		m_Info.Write(*m_OutStreamPtr);
	}
}

void NetworkManager::SendRejected()
{

}

void NetworkManager::SendFunction()
{

}

void ManagerInfo::Write(OutputMemoryBitStream& stream)
{
	stream.Write(name);
}

void ManagerInfo::Read(InputMemoryBitStream& stream)
{
	stream.Read(name);
}
