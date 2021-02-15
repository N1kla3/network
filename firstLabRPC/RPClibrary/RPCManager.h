//
// Created by nicola on 14/02/2021.
//

#pragma once

#include <string>
#include <unordered_map>
#include "Stream.h"

typedef void (*RPCWrapFunction)(class InputMemoryBitStream&);

namespace
{
    template<typename T>
    concept function = std::is_function<T>::value;
}

class RPCManager
{
public:
    RPCManager();
    virtual ~RPCManager();

    template<typename T, typename ...arg>
    requires function<T>
    void RegistrFunction(T function)
    {
        RPCWrapFunction func = [function](InputMemoryBitStream& stream){
            using arguments = std::tuple<arg...>;
            auto i = std::tuple_size<arguments>::value;
            for (int arguments_amount = 0; arguments_amount < i; arguments_amount++)
            {
                std::tuple_element_t<0, arguments> A;
                stream.Read(A);
                function(A);
            }
        };
    }

protected:
    uint32_t GetFreeID() const;

    uint32_t free_id;
    std::unordered_map<uint32_t, RPCWrapFunction> m_WrappedFunctions;
};
