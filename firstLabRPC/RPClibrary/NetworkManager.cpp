//
// Created by nicola on 22/02/2021.
//

#include "RPC.h"
#include "RPCManager.h"

#include "NetworkManager.h"


NetworkManager::NetworkManager(MANAGER_TYPE Type) :
	m_Type(Type)
{
}

NetworkManager::~NetworkManager()
{
}

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
