//
// Created by kolya on 3/19/21.
//
#include "functions.h"


std::vector<int> location{0,0,0};
std::vector<int> rotation{0,0,0};

void addToVector(const std::vector<int>& vector)
{
	if (vector.size() == 3)
	{
		for (int index = 0; index < 3; index++)
        {
			location[index] += vector[index];
		}
	}
	else
    {
		std::cout << "\n Incorrect vector\n";
	}
}

void setRotation(const std::vector<int>& vector)
{
    if (vector.size() == 3)
    {
        for (int index = 0; index < 3; index++)
        {
            rotation[index] += vector[index];
        }
    }
    else
    {
        std::cout << "\n Incorrect vector\n";
    }
}

void printVectors()
{
	std::cout << "\n location - ";
	for (auto el : location)
    {
		std::cout << el << ',';
	}
	std::cout << "\n rotation - ";
	for (auto el : rotation)
    {
		std::cout << el << ',';
	}
}
