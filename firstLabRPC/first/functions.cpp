//
// Created by kolya on 3/6/21.
//
#include "functions.h"

void function(int a, int b)
{
	LOG_INFO("function executed") << a;
}
void second(int a, const std::string& n)
{
	LOG_INFO("second executed") << n;
}
