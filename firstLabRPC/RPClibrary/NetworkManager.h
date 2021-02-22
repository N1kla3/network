//
// Created by nicola on 22/02/2021.
//

#pragma once

enum class MANAGER_TYPE
{
    SERVER,
    CLIENT
};

class NetworkManager
{
public:
    NetworkManager(MANAGER_TYPE Type);

    virtual ~NetworkManager();



protected:

};
