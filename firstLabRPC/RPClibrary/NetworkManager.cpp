//
// Created by nicola on 22/02/2021.
//

#include "RPC.h"
#include "Stream.h"
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

/** Client-Side only */
void NetworkManager::Connect(const std::string& address)
{
	if (m_Type == MANAGER_TYPE::CLIENT)
	{
		if (m_Socket->Connect(*SocketFactory::CreateIPv4FromString(address)) < 0)
		{
			LOG_ERROR(NetworkManager::Connect ) << address;
		}
		else bClientConnected = true;

		if (bClientConnected)
		{
			m_OutStreamPtr = std::make_unique<OutputMemoryBitStream>(OutputMemoryBitStream());
			SendHello();
			m_Socket->Send(m_OutStreamPtr->GetBufferPtr(), m_OutStreamPtr->GetByteLength());

			m_Socket->SetBlocking();
			char buffer[32];
			for (int i = 0; i < 5; i++)
			{
				int received = m_Socket->Receive(buffer, 1);
				if (received > 0)
				{
					m_InStreamPtr = std::make_unique<InputMemoryBitStream>(buffer, GetRequiredBits<PACKET::MAX>::VALUE);
					PACKET packet;
					m_InStreamPtr->Read(packet);
					if (packet == HELLO)
					{
						LOG_INFO(Connected to Server);
						bClientApproved = true;
					}
					else if (packet == REJECT)
					{
						LOG_INFO(Server reject you);
						bClientConnected = false;
					}
				}
				else
				{
					LOG_INFO(wait responce - ) << i;
					sleep(1);
				}
			}
		}
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

/** Server-Only */
void NetworkManager::HandleHelloPacket(const TCPSocketPtr& socket)
{
	if (m_Type == MANAGER_TYPE::SERVER)
	{
		ManagerInfo info;
		info.Read(*m_InStreamPtr);

		bool validation = false;
		if      (m_Level == SECURITY_LEVEL::LOW) validation = ValidateLowLevel(info);
		else if (m_Level == SECURITY_LEVEL::COMMON) validation = ValidateCommonLevel(info);
		else if (m_Level == SECURITY_LEVEL::HIGH) validation = ValidateHighLevel(info);

		if (validation)
		{
			OutputMemoryBitStream stream;
			stream.WriteBits(PACKET::HELLO, GetRequiredBits<PACKET::MAX>::VALUE);
			socket->Send(stream.GetBufferPtr(), stream.GetByteLength());
			m_ServerConnections->push_back(socket);
			LOG_INFO(Client added to clients - ) << info.name;
		}
		else
		{
			LOG_WARNING(Client rejected level validation ) << info.name;
			SendRejected(socket);
		}
	}
}

/** Client-Side only */
void NetworkManager::HandleRejectedPacket()
{

}

void NetworkManager::HandleFunctionPacket()
{

}

/** Write to member streams */
void NetworkManager::SendHello()
{
	m_OutStreamPtr->WriteBits(PACKET::HELLO, GetRequiredBits<PACKET::MAX>::VALUE);
	if (m_Type == MANAGER_TYPE::CLIENT)
	{
		m_Info.Write(*m_OutStreamPtr);
	}
}

void NetworkManager::SendRejected(TCPSocketPtr socket)
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
