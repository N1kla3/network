//
// Created by kolya on 3/6/21.
//
#include "functions.h"

int number = 0;

void increaseNumber(int add)
{
    number += add;
	updated = true;
}

void answer()
{
	std::cout << "\nNumber now is " << number << " *(/\n";
	updated = false;
}
