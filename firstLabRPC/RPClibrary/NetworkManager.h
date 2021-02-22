//
// Created by nicola on 22/02/2021.
//

#pragma once

struct manager_info
{
    std::string name;

};

enum PACKET
{
    HELLO,
    REJECT,
    FUNCTION,
    MAX
};

enum class MANAGER_TYPE
{
    SERVER,
    CLIENT
};

enum class MANAGER_MODE
{
    MANUAL,
    FREQUENCY
};
/**
 * @brief
 */
class NetworkManager
{
public:
    NetworkManager(MANAGER_TYPE Type);

    virtual ~NetworkManager();

    template<typename T>
    void AddDataToPacket(T value)
    {

    }

    void CreatePacket();

    void SendPacket();

    void ReceivePacket();

    /** @brief Check received data per second */
    void SetNetFrequency(float frequency);

    inline void HaveReceivedData() const noexcept;

    void SetManagerMode(MANAGER_MODE mode) const;

    MANAGER_MODE GetManagerMode() const;

    void Connect(const std::string& address);

    void Tick(float deltaTime);

protected:

    bool bContainSendData = false;

    bool bContainReceiveData = false;

    float m_NetFrequency = 1.f;

    MANAGER_MODE m_Mode = MANAGER_MODE::FREQUENCY;
};
